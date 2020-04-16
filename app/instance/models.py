from django.db import models
from app.mission.models import Mission
from app.team.models import Team, Operation


class Instance(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)


class InstanceRoom(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    pass


class InstanceObject(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    pass


class InstanceNpc(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    pass


class InstanceLog(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    INSTANCE_LOG_TYPE_CHOICE = (
        ('mov', 'Movement'),
        ('int', 'Interaction'),
        ('com', 'Combat'),
    )
    type = models.CharField(max_length=3, choices=INSTANCE_LOG_TYPE_CHOICE, default='mov')
    message = models.CharField(max_length=255, default='')
    datetime_logged = models.DateTimeField(auto_now_add=True)

