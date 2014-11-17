from hello.models.cron import set_interval, timed_job
set_interval(timed_job(), 10)