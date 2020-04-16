from django.contrib import admin
from app.character import models


class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'character_class', 'name')


admin.site.register(models.Character, CharacterAdmin)


class CharacterClassAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.CharacterClass, CharacterClassAdmin)


class PerkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(models.Perk, PerkAdmin)


class QuirkAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(models.Quirk, QuirkAdmin)


class CharacterSkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.CharacterSkill, CharacterSkillAdmin)