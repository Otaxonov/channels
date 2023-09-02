from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from gs2.models import Group, Chat
from channels.db import database_sync_to_async
from time import sleep
import asyncio
import json

# Sync Consumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...")

        self.group_name = self.scope['url_route']['kwargs']['group_name']

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message Received from Client:", event)

        data = json.loads(event['text'])
        group = Group.objects.get(name=self.group_name)

        if self.scope['user'].is_authenticated:
            chat = Chat(group=group, content=data['msg'])
            chat.save()

            data['user'] = self.scope['user'].username

            async_to_sync(self.channel_layer.group_send)(self.group_name, {
                'type': 'chat.message',
                'message': json.dumps(data)
            })
        else:
            self.send({
            'type': 'websocket.send',
            'text': json.dumps({"msg": "Login Required", "user": "unknown"})
            })

    def chat_message(self, event):
        print("Event:", event)

        self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)
        raise StopConsumer()

# Async Consumer
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected...")

        self.group_name = self.scope['url_route']['kwargs']['group_name']

        await self.channel_layer.group_add(self.group_name, self.channel_name)

        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Message Received from Client:", event)

        data = json.loads(event['text'])
        group = await database_sync_to_async(Group.objects.get)(name=self.group_name)

        if self.scope['user'].is_authenticated:
            chat = Chat(group=group, content=data['msg'])
            await database_sync_to_async(chat.save)()

            data['user'] = self.scope['user'].username

            await self.channel_layer.group_send(self.group_name, {
                'type': 'chat.message',
                'message': json.dumps(data)
            })
        else:
            await self.send({
            'type': 'websocket.send',
            'text': json.dumps({"msg": "Login Required", "user": "unknown"})
            })

    async def chat_message(self, event):
        print("Event:", event)

        await self.send({
            'type': 'websocket.send',
            'text': event['message']
        })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        raise StopConsumer()
