#!/usr/bin/env python
import os
import sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
    
    from apscheduler.schedulers.blocking import BlockingScheduler
    from hello.cron import timed_job
    sched = BlockingScheduler()
    # Schedule timed_job to be called every 5 seconds
    sched.add_job(timed_job, 'interval', seconds=5)

    sched.start()

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)