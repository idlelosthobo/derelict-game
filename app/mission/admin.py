from django.contrib import admin
from app.mission import models


admin.register(models.Mission)
admin.register(models.MissionObject)
admin.register(models.MissionRoom)
admin.register(models.MissionRoomObject)
