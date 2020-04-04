from django.contrib import admin
from app.player import models


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(models.Player, PlayerAdmin)