from django.urls import path
from gs3 import consumers

websocket_urlpatterns = [
    path('ws/sc/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/ac/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]