from django.db import models
from django.contrib.auth.models import User


class CharacterClass(models.Model):
    name = models.CharField(max_length=16, default='')


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, default='')


