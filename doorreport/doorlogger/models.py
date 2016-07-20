from django.db import models
from datetime import datetime 

class Door(models.Model):
	door_name = models.CharField(max_length=200)

class Event(models.Model):
	door = models.ForeignKey(Door, on_delete=models.CASCADE)
	event_type = models.CharField(max_length=20)
	open_level = models.IntegerField(default=0)
	time_stamp = models.DateTimeField(default=datetime.now, blank=True)
