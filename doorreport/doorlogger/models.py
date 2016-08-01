from django.db import models
from datetime import datetime 

class Door(models.Model):
	door_name = models.CharField(max_length=144)
	door_type = models.CharField(max_length=35)

	def __str__(self):
		return self.door_name

class Event(models.Model):
	door = models.ForeignKey(Door, on_delete=models.CASCADE)
	event_type = models.CharField(max_length=20)
	open_level = models.IntegerField(default=0)
	time_stamp = models.DateTimeField('time stamp')
	
	def __str__(self):
		
		return ("%s: %d" % (self.event_type, self.open_level)) 