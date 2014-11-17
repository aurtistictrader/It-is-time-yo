from django_cron import cronScheduler, Job
from .models import Reminder
from datetime import datetime

class refreshDatabse(Job):
	"""
	Cron Job that checks the lgr users mailbox and adds any 
	approved senders' attachments to the db
	"""

	# run every 30 seconds
	run_every = 30
		
	def job(self):
		# This will be executed every 30 seconds
		# Query into DB and then look for date_left that are past current date
        lookup_users = Reminder.objects.raw(''' SELECT username, message
												FROM hello_reminder 
												WHERE (	time_left <= (SELECT current_time) AND 
														date_left = (SELECT current_date)) OR 
														date_left < (SELECT current_date)''')
		
		# Now grab this data and YO it
        for user,msg in lookup_users:
        	# do stuff here

		# Finally delete it
        Reminder.objects.raw('''DELETE 	FROM hello_reminder 
										WHERE (	time_left <= (SELECT current_time) AND 
												date_left = (SELECT current_date)) OR 
												date_left < (SELECT current_date)''')

cronScheduler.register(refreshDatabse)