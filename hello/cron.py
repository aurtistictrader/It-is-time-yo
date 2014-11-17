from hello.model import Reminder
from django_cron import CronJobBase, Schedule

class RefreshDatabase(CronJobBase):
    RUN_EVERY_MINS = 1 # every minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'hello.refresh_database'    # a unique code

    def do(self):
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
        pass    # do your thing here