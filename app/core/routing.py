from django.urls import re_path

from app.core import consumers

websocket_urlpatterns = [
    re_path(r'ws/heartbeat/', consumers.HeartBeatConsumer),
]