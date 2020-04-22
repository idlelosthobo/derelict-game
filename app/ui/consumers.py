import json
from channels.generic.websocket import JsonWebsocketConsumer, SyncConsumer, AsyncConsumer
from app.chat.models import Message
from django.core.serializers import serialize


class InterfaceConsumer(JsonWebsocketConsumer):
    pass