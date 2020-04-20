import json
from channels.generic.websocket import WebsocketConsumer, SyncConsumer, AsyncConsumer
from app.chat.models import Message
from django.core.serializers import serialize


class HeartBeatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))


class EchoConsumer(SyncConsumer):

    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })

    def websocket_disconnect(self, event):
        self.send({
            "type": "websocket.disconnect",
        })

    def websocket_receive(self, event):
        text_data_json = json.loads(event['text'])

        if text_data_json['action'] == 'get_messages':

            message = Message()
            message.user = self.scope['user']
            if text_data_json['message'][:2] == '/g':
                message.type = 'glo'
                message.message = text_data_json['message'][2:]
            elif text_data_json['message'][:2] == '/m':
                message.type = 'mar'
                message.message = text_data_json['message'][2:]
            else:
                message.message = text_data_json['message']
            message.save()

            message_list = Message.objects.all()

            self.send({
                "type": "websocket.send",
                "text": serialize('json', message_list),
            })


class EchoAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })