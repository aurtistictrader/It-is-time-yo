from django_cron import cronScheduler, Job

# This is a function I wrote to check a feedback email address
# and add it to our database. Replace with your own imports


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
		# Now grab this data and YO it

		# Finally delete it
		"""
			SQL: 
			delete from hello_reminder where date_left < (select current_date);
			delete from hello_reminder where time_left < (select current_time) and date_left = (select current_date);
		"""

cronScheduler.register(refreshDatabse)