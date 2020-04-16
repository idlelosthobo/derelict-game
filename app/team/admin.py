from django.contrib import admin
from app.team import models


admin.site.register(models.Operation)
admin.site.register(models.Team)
admin.site.register(models.TeamCharacter)