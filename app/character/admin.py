from django.contrib import admin
from app.character import models


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'character_class', 'name')


admin.site.register(models.Character, CharacterAdmin)
