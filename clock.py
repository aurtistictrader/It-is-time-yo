from apscheduler.schedulers.blocking import BlockingScheduler
import requests

def timed_job():
    requests.get("http://itistimeyo.me/ghettoping", data={})

sched = BlockingScheduler()
# Schedule timed_job to be called every 5 seconds
sched.add_job(timed_job, 'interval', seconds=5)

sched.start()