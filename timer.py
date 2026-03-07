from datetime import datetime
import time
import os

class Timer:
    def __init__(self, notif_obj):
        self.notification = notif_obj

    def calculate_wait_time(self, target_time) -> float:
        """Calculate the number of seconds to wait until the target time."""
        now = datetime.now()
        target = datetime.strptime(target_time, "%I:%M %p").replace(year=now.year, month=now.month, day=now.day)
        if target < now:
            target = target.replace(day=now.day + 1)  # Adjust for next day
        return (target - now).total_seconds()
    
    def countdown_timer(self, wait_time, target_time, program_name):
        """Display a countdown timer until the target time."""
        while wait_time > 0:            
            minutes, seconds = divmod(int(wait_time), 60)
            hours, minutes = divmod(minutes, 60)
            
            time.sleep(60)
            wait_time -= 60

            return f"<< {program_name} >>Time remaining until {target_time}: {hours:02d}:{minutes:02d}:00"
    
    def format_time(self, seconds):
        """return %M:%S formated string of float seconds recieved as arg"""
        return time.strftime("%M:%S", time.gmtime(seconds))