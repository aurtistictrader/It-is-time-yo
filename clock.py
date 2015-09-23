from apscheduler.schedulers.blocking import BlockingScheduler
from hello.models import Reminder
from django.db import connection
import requests

sched = BlockingScheduler()

@sched.timed_job('interval', seconds=5)
def timed_job():
    api_token = "85f098d7-25c4-404f-baa5-ca0e0d21583c"
    # This will be executed every 30 seconds
    # Query into DB and then look for date_left that are past current date
    lookup_users = Reminder.objects.raw(''' SELECT username,id
                                            FROM hello_reminder
                                            WHERE (	time_left <= (SELECT current_time) AND
                                                    date_left = (SELECT current_date)) OR
                                                    date_left < (SELECT current_date)''')
    for users in lookup_users:
        requests.post("http://api.justyo.co/yo/", data={'api_token': api_token, 'username': str(users.username).upper()})

    # Now grab this data and YO it
    # for user,msg in lookup_users:
    # do stuff here

    # Finally delete it
    cursor = connection.cursor()
    cursor.execute('''DELETE FROM hello_reminder WHERE (  time_left <= (SELECT current_time) AND date_left = (SELECT current_date)) OR date_left < (SELECT current_date)''')
    connection.commit()
    pass

sched.start()