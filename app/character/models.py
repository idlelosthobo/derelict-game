from django.db import models
from django.contrib.auth.models import User


class Perk(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name;


class Quirk(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name;


class Aspect(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default = '')
    perk_1 = models.ForeignKey(Perk, on_delete=models.CASCADE, related_name='perk_1')
    perk_2 = models.ForeignKey(Perk, on_delete=models.CASCADE, related_name='perk_2')
    perk_3 = models.ForeignKey(Perk, on_delete=models.CASCADE, related_name='perk_3')
    quirk_1 = models.ForeignKey(Quirk, on_delete=models.CASCADE, related_name='quirk_1')
    quirk_2 = models.ForeignKey(Quirk, on_delete=models.CASCADE, related_name='quirk_2')
    quirk_3 = models.ForeignKey(Quirk, on_delete=models.CASCADE, related_name='quirk_3')

    def __str__(self):
        return self.name;


class Alignment(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name;


class CharacterClass(models.Model):
    name = models.CharField(max_length=16, default='', unique=True)

    def __str__(self):
        return self.name;


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    aspect = models.ForeignKey(Aspect, on_delete=models.CASCADE, blank=True, null=True)
    alignment = models.ForeignKey(Alignment, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=16, default='', unique=True)

    def __str__(self):
        return self.name;


