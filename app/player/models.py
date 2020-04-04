from django.db import models
from django.contrib.auth.models import User
from app.character.models import Character


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
