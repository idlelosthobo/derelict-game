from django.urls import re_path
from app.game.consumers import GameConsumer

game_websocket_urlpatterns = [
    re_path(r'ws/game/', GameConsumer),
]