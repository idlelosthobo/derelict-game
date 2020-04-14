from django.db import models
from django.contrib.auth.models import User
from app.character.models import Character
from app.team.models import Operation, Team


class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, default='')


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE, blank=True, null=True)
    to_character = models.ForeignKey(Character, related_name='to_character', on_delete=models.CASCADE, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, blank=True, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, blank=True, null=True)
    MESSAGE_TYPE_CHOICE = (
        ('dir', 'Direct'),
        ('cha', 'Channel'),
        ('org', 'Organize'),
        ('tra', 'Trade'),
        ('glo', 'Global'),
        ('sys', 'System'),
    )
    type = models.CharField(max_length=3, choices=MESSAGE_TYPE_CHOICE, default='dir')
    MESSAGE_STYLE_CHOICE = (
        ('pri', 'Primary'),
        ('sec', 'Secondary'),
        ('war', 'Warning'),
    )
    style = models.CharField(max_length=3, choices=MESSAGE_STYLE_CHOICE, default='pri')
    message = models.CharField(max_length=256, default='')
    date_entered = models.DateTimeField(auto_now_add=True)