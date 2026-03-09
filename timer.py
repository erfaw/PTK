from datetime import datetime
import time
import pytz

class Timer:
    def __init__(self, notif_obj):
        self.notification = notif_obj
        self.time_zone = pytz.timezone('Asia/Tehran')

    def calculate_wait_time(self, target_time) -> float:
        """Calculate the number of seconds to wait until the target time."""
        now = datetime.now()
        target = datetime.strptime(target_time, "%I:%M %p").replace(year=now.year, month=now.month, day=now.day)
        if target < now:
            target = target.replace(day=now.day + 1)  # Adjust for next day
        return (target - now).total_seconds()
    
    def format_time(self, seconds):
        """return %M:%S formated string of float seconds recieved as arg"""
        return time.strftime("%H:%M:%S", time.gmtime(seconds))
    
    def get_now(self):
        return datetime.now(tz= self.time_zone).time()