from django.db import models
from app.character.models import CHARACTER_STAT_DECIMALS, CHARACTER_STAT_DIGITS


class Npc(models.Model):
    NPC_TYPE_CHOICE = (
        ('fri', 'Friendly'),
        ('hos', 'Hostile'),
    )
    type = models.CharField(max_length=3, choices=NPC_TYPE_CHOICE, default='hos')
    NPC_RANK_CHOICE = (
        ('a', 'A: Does not move and harmless.'),
        ('b', 'B: Moves and harmless.'),
        ('c', 'C: Does not move and cause close range harm.'),
        ('d', 'D: Moves and can cause close range harm.'),
        ('e', 'E: Does not move and can cause long range harm.'),
        ('f', 'F: moves and can long range harm'),
    )
    rank = models.CharField(max_length=3, choices=NPC_RANK_CHOICE, default='a')
    name = models.CharField(max_length=16, default='', unique=True)
    brute = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    finesse = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    brilliance = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    grit = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
    expertise = models.DecimalField(max_digits=CHARACTER_STAT_DIGITS, decimal_places=CHARACTER_STAT_DECIMALS, default=0)
