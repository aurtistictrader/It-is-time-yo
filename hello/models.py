from django.db import models

# Create your models here. 
class Reminder(models.Model):
	username = models.CharField(max_length=128)
	message = models.CharField(max_length=400)
	date_created = models.DateTimeField('date created')
	time_created = models.DateTimeField('time created')
	date_left = models.DateTimeField('date reminded')
	time_left = models.DateTimeField('time reminded')