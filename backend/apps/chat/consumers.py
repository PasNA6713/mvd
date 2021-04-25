import json

from channels.generic.websocket import WebsocketConsumer


CURRENT_CHATS = dict()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        token = self.scope['url_route']['kwargs']['token']
        CURRENT_CHATS[token] = self.channel_name
        self.accept()

    def disconnect(self, close_code):
        for i, j in CURRENT_CHATS.items():
            if j == self.channel_name:
                CURRENT_CHATS.pop(i)

    # отправка
    def chat_message(self, event):
        self.send(text_data=event["message"])

    # принятие
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
