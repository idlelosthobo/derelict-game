from django.contrib import admin
from app.chat import models


class ChannelAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Channel, ChannelAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'character', 'message', 'date_entered')


admin.site.register(models.Message, MessageAdmin)


