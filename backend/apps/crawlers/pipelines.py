import copy
from datetime import datetime, timedelta

from bs4 import BeautifulSoup as BS
from scrapy.exceptions import DropItem
from loguru import logger

from django.conf import settings
from .spiders.core.services import extract_domain, to_datetime
from apps.chat.services import a_send_all
from apps.chat.tasks import celery_send_all


class PreprocessPipeline():
    def __init__(self):
        self.urls = set()

    def open_spider(self, spider): pass

    def close_spider(self, spider): pass

    def process_item(self, item, spider):
        if item['link'] in self.urls:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.urls.add(item['link'])
        
        item['text'] = BS(item.get('text'), features="lxml").text

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


class PostgresPipeline():
    def open_spider(self, spider):
        logger.success(f'Run spider: {spider.name.upper()}')

    def close_spider(self, spider):
        logger.success(f'{spider.name.upper()} finished!')
        logger.success(f'Scraped: {len(self.urls)} items.')
    
    def process_item(self, item, spider):
        celery_send_all.delay(item['title'])
        # source = extract_domain(item['link'])
        # h = PostModel.objects.get_or_create(
        #     link=item['link'], title=item['title'],
        #     posted=item['posted'], text=item['text'],
        #     source=source
        # )
        # model, isCreated = copy.deepcopy(h[0]), h[1]
        # if isCreated:
        #     model.tags = item.get('tags')
        #     logger.info(f'Created - {model}')
        # else:
        #     if len(model.datetime) >= settings.PARSER_COUNTER:
        #         return item
        #     logger.info(f'Updated - {model}')
        # model.likes.append(item.get('likes'))
        # model.bookmarks.append(item.get('bookmarks'))
        # model.views.append(item.get('views'))
        # model.datetime.append(item.get('datetime'))
        # model.comments.append(item.get('comments'))
        # model.save()
        return item