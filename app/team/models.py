from django.db import models
from app.character.models import Character


class Operation(models.Model):
    name = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.name


class Team(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=16, default='')

    def __str__(self):
        return self.name


class TeamCharacter(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    leader = models.BooleanField(default=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return self.character.name
