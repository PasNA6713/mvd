from config.celery import app

from .services import send_to_all, send_to_user
 

@app.task(name='tasks.celery_send_all')
def celery_send_all(message: str):
    send_to_all(message)

@app.task(name='tasks.celery_send_user')
def celery_send_user(channel_name, message: str):
    send_to_user(channel_name, message)