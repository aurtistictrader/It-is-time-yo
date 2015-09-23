from apscheduler.schedulers.blocking import BlockingScheduler
from hello.cron import timed_job

sched = BlockingScheduler()
# Schedule timed_job to be called every 5 seconds
sched.add_job(timed_job, 'interval', seconds=5)

sched.start()