from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
from gs2.models import Group, Chat
import asyncio
import json


class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected...")

        self.group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message Received from Client:", text_data)

        data = json.loads(text_data)
        message = data['msg']

        group = Group.objects.get(name=self.group_name)

        if self.scope['user'].is_authenticated:
            chat = Chat(group=group, content=message)
            chat.save()

            data['user'] = self.scope['user'].username

            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                'type': 'chat.message',
                'message': message,
                'user': data['user']
            })
        else:
            self.send(text_data=json.dumps({"msg": "Login Required", "user": "guest"}))

    def chat_message(self, event):
        print("Event:", event)

        self.send(text_data=json.dumps({
            'msg': event['message'],
            'user': event['user']
        }))

    def disconnect(self, code):
        print("Websocket Disconnected...", code)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        print("Message Received from Client:", text_data)
        for i in range(10):
            await self.send(text_data=json.dumps({"count": i}))
            await asyncio.sleep(1)

    async def disconnect(self, code):
        print("Websocket Disconnected...", code)