from django.db import models


class Mission(models.Model):
    name = models.CharField(max_length=32, default='')


class MissionObject(models.Model):
    name = models.CharField(max_length=32, default='')
    MISSION_OBJECT_POSITION_CHOICE = (
        ('flo', 'Floor'),
        ('roo', 'Roof'),
        ('nor', 'North'),
        ('eas', 'East'),
        ('sou', 'South'),
        ('wes', 'West'),
    )
    position = models.CharField(max_length=3, choices=MISSION_OBJECT_POSITION_CHOICE, default='flo')
    MISSION_OBJECT_VISIBILITY_CHOICE = (
        ('vis', 'Visible'),
        ('hid', 'Hidden'),
        ('inv', 'Invisible'),
    )
    visibility = models.CharField(max_length=3, choices=MISSION_OBJECT_VISIBILITY_CHOICE, default='vis')


class MissionRoom(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)
    MISSION_ROOM_SECTION_CHOICE = (
        ('wal', 'Wall'),
        ('doo', 'Door'),
        ('ope', 'Open'),
    )
    north = models.CharField(max_length=3, choices=MISSION_ROOM_SECTION_CHOICE, default='wal')
    east = models.CharField(max_length=3, choices=MISSION_ROOM_SECTION_CHOICE, default='wal')
    south = models.CharField(max_length=3, choices=MISSION_ROOM_SECTION_CHOICE, default='wal')
    west = models.CharField(max_length=3, choices=MISSION_ROOM_SECTION_CHOICE, default='wal')


class MissionRoomObject(models.Model):
    mission_room = models.ForeignKey(MissionRoom, on_delete=models.CASCADE)
    mission_object = models.ForeignKey(MissionObject, on_delete=models.CASCADE)
