from .models import Reminder
import threading
from django.db import connection

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def timed_job():

    # This will be executed every 30 seconds
	# Query into DB and then look for date_left that are past current date
    lookup_users = Reminder.objects.raw(''' SELECT username
											FROM hello_reminder 
											WHERE (	time_left <= (SELECT current_time) AND 
													date_left = (SELECT current_date)) OR 
													date_left < (SELECT current_date)''')
	
	# Now grab this data and YO it
    # for user,msg in lookup_users:
    # do stuff here

	# Finally delete it
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM hello_reminder WHERE (  time_left <= (SELECT current_time) AND date_left = (SELECT current_date)) OR date_left < (SELECT current_date)''')
    connection.commit()
    pass