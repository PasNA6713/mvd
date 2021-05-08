import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import SessionModel


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        token = self.scope['url_route']['kwargs']['token']
        session, is_created = await database_sync_to_async(SessionModel.objects.get_or_create)(token=token)
        session.session = self.channel_name
        await database_sync_to_async(session.save)()
        await self.accept()

    async def disconnect(self, close_code):
        session = await database_sync_to_async(SessionModel.objects.get)(session=self.channel_name)
        await database_sync_to_async(session.delete)()
        await self.close()

    # отправка
    async def chat_message(self, event):
        await self.send(event["message"])

    # принятие
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
