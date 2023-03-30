import schedule
import time


def scheule_a_job(type, interval, method):
    if type == "Mins":
        schedule.every(interval).minutes.do(method)

    if type == "Secs":
        schedule.every(interval).seconds.do(method)

    if (interval == "Hrs"):
        schedule.every().hour.do(method)

    if (interval == "Daily"):
        schedule.every().day.at("10:00").do(method)

    while True:
        schedule.run_pending()
        time.sleep(1)


class SchedulerUtils:
    pass
