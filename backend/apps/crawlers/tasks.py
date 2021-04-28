from config.celery import app

from apps.chat.tasks import celery_send_all
from .spiders.core.instagram_parser import insta_parse
 

@app.task(name='tasks.insta_parser')
def insta_parser(number, tag):
    for i, message in zip(range(number), insta_parse(tag)):
        celery_send_all.delay(message)