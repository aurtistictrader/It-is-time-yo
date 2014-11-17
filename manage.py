#!/usr/bin/env python
import os
import sys
from hello.models.cron import set_interval, timed_job
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line

    set_interval(timed_job(), 10)
    execute_from_command_line(sys.argv)
