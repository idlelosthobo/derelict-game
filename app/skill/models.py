from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=32, default='')
    SKILL_TYPE_CHOICE = (
        ('att', 'Attack'),
        ('mov', 'Movement'),
        ('sup', 'Support'),
        ('hea', 'Heal'),
        ('int', 'Interaction'),
    )
    type = models.CharField(max_length=3, choices=SKILL_TYPE_CHOICE, default='att')
    range = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
