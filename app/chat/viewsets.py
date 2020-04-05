from rest_framework import viewsets
from app.chat import models
from app.chat import serializers


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all().order_by('-id')
    serializer_class = serializers.MessageSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
