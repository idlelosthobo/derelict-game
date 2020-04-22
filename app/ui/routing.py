from django.urls import re_path
from app.ui.consumers import InterfaceConsumer

ui_websocket_urlpatterns = [
    re_path(r'ws/ui/', InterfaceConsumer),
]