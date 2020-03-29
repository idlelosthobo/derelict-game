from django.contrib import admin
from app.chat import models


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'character', 'message', 'date_entered')


admin.site.register(models.Message, MessageAdmin)
