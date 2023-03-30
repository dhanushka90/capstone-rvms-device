import datetime


class DateTimeUtils:

    def getCurrentTimeStamp(self):
        current_time = datetime.datetime.now()
        current_time_stamp = current_time.timestamp()
        return str(int(current_time_stamp))
