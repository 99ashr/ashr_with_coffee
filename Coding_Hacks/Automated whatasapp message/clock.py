#!/usr/bin/env python3

#! --------------------------------- Scheduler -------------------------------- #
from apscheduler.schedulers.blocking import BlockingScheduler
from send_daily_status import daily_status_report


sched = BlockingScheduler()
sched.add_job(func=daily_status_report, trigger='cron', hour='04', minute="52")
sched.start()
#! ------------------------------------ EOF ----------------------------------- #
