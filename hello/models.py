from django.db import models

# Create your models here. 
class Reminder(models.Model):
	username = models.CharField(max_length=128)
	message = models.CharField(max_length=400)
	time_created = models.DateTimeField('date created', auto_now_add=True)
	time_left = models.DateTimeField('date created', auto_now_add=True)