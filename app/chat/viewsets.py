from rest_framework import viewsets
from app.chat import models
from app.chat import serializers


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer