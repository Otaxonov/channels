from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from time import sleep
import asyncio
import json


class MyWebsocketConsumer(WebsocketConsumer):
    def connect(self):
        print("Websocket Connected...")
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        print("Message Received from Client:", text_data)
        for i in range(10):
            self.send(text_data=json.dumps({"count": i}))
            sleep(1)

    def disconnect(self, code):
        print("Websocket Disconnected...", code)


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
