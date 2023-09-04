from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from time import sleep
import asyncio


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("Websocket Connected...")
        self.accept()

    def receive_json(self, content, **kwargs):
        print("Message Received from Client:", content)

        for i in range(10):
            self.send_json({"message": f"Message Sent to Client #{i}"})
            sleep(1)

    def disconnect(self, code):
        print("Websocket Disconnected...", code)


class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print("Websocket Connected...")
        await self.accept()

    async def receive_json(self, content, **kwargs):
        print("Message Received from Client:", content)
        for i in range(10):
            await self.send_json({"message": f"Message Sent to Client #{i}"})
            await asyncio.sleep(1)

    async def disconnect(self, code):
        print("Websocket Disconnected...", code)
