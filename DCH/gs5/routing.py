from django.urls import path
from gs5 import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MyJsonWebsocketConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi()),
]