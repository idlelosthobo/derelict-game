import json
from channels.generic.websocket import JsonWebsocketConsumer, SyncConsumer, AsyncConsumer
from app.chat.models import Message
from django.core.serializers import serialize


class ChatConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        self.disconnect(code)

    def receive_json(self, content, **kwargs):

        if content['action'] == 'send_message':

            message = Message()
            message.user = self.scope['user']
            if content['message'][:2] == '/g':
                message.type = 'glo'
                message.message = content['message'][2:]
            elif content['message'][:2] == '/m':
                message.type = 'mar'
                message.message = content['message'][2:]
            else:
                message.message = content['message']
            message.save()

            message_list = Message.objects.all()

            self.send(serialize('json', message_list))


