from django.urls import re_path

from app.core import consumers

websocket_urlpatterns = [
    re_path(r'ws/heart_beat/', consumers.HeartBeatConsumer),
    re_path(r'ws/echo/', consumers.EchoConsumer),
]