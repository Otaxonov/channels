from django.urls import path
from gs4 import consumers

websocket_urlpatterns = [
    path('ws/sc/<str:group_name>/', consumers.MyWebsocketConsumer.as_asgi()),
    path('ws/ac/<str:group_name>/', consumers.MyAsyncWebsocketConsumer.as_asgi()),
]