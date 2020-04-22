from django.urls import re_path
from app.chat.consumers import ChatConsumer

chat_websocket_urlpatterns = [
    re_path(r'ws/chat', ChatConsumer),
]