from rest_framework import routers
from app.chat import viewsets


router = routers.DefaultRouter()
router.register(r'message', viewsets.MessageViewSet)
