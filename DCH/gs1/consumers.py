from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from time import sleep
import asyncio
import json

# Sync Consumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Websocket Connected...")
        print("Channel Layer:", self.channel_layer)

        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Message received from Client:", event['text'])
        for i in range(10):
            self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": i})
            })
            sleep(2)

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()

# Async Consumer
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Websocket Connected...")
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Message received from Client:", event['text'])
        for i in range(10):
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({"count": i})
            })
            await asyncio.sleep(2)

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()
