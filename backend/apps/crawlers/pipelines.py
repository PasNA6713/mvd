import os
import joblib
from datetime import datetime, timedelta

from asgiref.sync import sync_to_async
from bs4 import BeautifulSoup as BS
from scrapy.exceptions import DropItem

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

from django.conf import settings
from apps.chat.tasks import celery_send_all

from .spiders.core.services import extract_domain, to_datetime
from .models import NewsModel
from .mlearn.preproccesor import preproccesor, ner

from loguru import logger

rf_news = joblib.load(os.path.join(settings.BASE_DIR,'apps/crawlers/mlearn/news_bin_class.pkl'))
tf_news = joblib.load(os.path.join(settings.BASE_DIR,'apps/crawlers/mlearn/news_tf.pkl'))


class PreprocessPipeline():
    def __init__(self): self.urls = set()

    def open_spider(self, spider): 
        logger.success(f'Run spider: {spider.name.upper()}')

    def close_spider(self, spider): 
        logger.success(f'{spider.name.upper()} finished!')
        logger.success(f'Scraped: {len(self.urls)} items.')

    def process_item(self, item, spider):
        if item['link'] in self.urls:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.urls.add(item['link'])

        if item.get('text') is None or item.get('link') is None:
            raise DropItem(f"Empty item!")
        
        # item['text'] = BS(item.get('text'), features="lxml").text
        if item['text']:
            for i in BS(item['text']).find_all('img'):
                item['text'] = item['text'].replace(i, '')


        if item.get('posted'):
            try:
                item['posted'] = datetime.strptime(item.get('posted'), "%Y-%m-%dT%H:%M:%S%z")
            except Exception:
                posted = item.get('posted').replace('Создано: ', '')
                posted = posted.replace('Обновлено: ', '')
                if 'вчера' in posted.lower():
                    posted = posted.replace('вчера в ', '').split(':')
                    now = datetime.now()
                    yesterday = now - timedelta(days=1)
                    item['posted'] = now.replace(day=yesterday.day, hour=int(posted[0]), minute=int(posted[1]), second=0, microsecond=0)

                elif 'сегодня' in posted.lower():
                    posted = posted.replace('сегодня в ', '').split(':')
                    now = datetime.now()
                    item['posted'] = now.replace(hour=int(posted[0]), minute=int(posted[1]), second=0, microsecond=0)

                elif ',' in posted:
                    time, date = item['posted'].split(',')
                    item['posted'] = to_datetime(date.strip(), *list(map(lambda x: int(x), time.split(":"))))

                else:
                    item['posted'] = to_datetime(posted)
        return item


class ClassificationPipeline():
    def open_spider(self, spider): pass

    def close_spider(self, spider): pass

    def process_item(self, item, spider):
        text = BS(item.get('text'), features="lxml").text
        # text = item.get('text')
        if rf_news.predict(tf_news.transform([preproccesor(text)]))==0:
            suhnosti = ner(text)
            item['loc'] = suhnosti[0]
            item['org'] = suhnosti[1]
            item['per'] = suhnosti[2]
            return item
        else: raise DropItem(f"Not interested news")


class PostgresPipeline():
    def open_spider(self, spider): pass

    def close_spider(self, spider): pass
    
    async def process_item(self, item, spider):
        model, is_created = await sync_to_async(NewsModel.objects.get_or_create)(**item)
        celery_send_all.delay({
            "text": item['title'],
            "source": item['link'],
            'posted': item['posted'],
            "id": model.id
        })
        return item