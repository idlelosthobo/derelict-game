from django.db import models
from django.contrib.auth.models import User
from app.skill.models import Skill

CHARACTER_STAT_DIGITS = 4
CHARACTER_STAT_DECIMALS = 1


class Perk(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Quirk(models.Model):
    name = models.CharField(max_length=32, default='', unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=16, default='', unique=True)
    brute = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    finesse = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    brilliance = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    grit = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    expertise = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)

    def __str__(self):
        return self.name


class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, default='', unique=True)
    brute = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    finesse = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    brilliance = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    grit = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    expertise = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CharacterSkill(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rank = models.IntegerField(default=1)
