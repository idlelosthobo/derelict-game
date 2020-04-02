from django.contrib import admin
from app.character import models


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'character_class', 'name')


admin.site.register(models.Character, CharacterAdmin)


class CharacterClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.CharacterClass, CharacterClassAdmin)
