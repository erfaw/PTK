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
        # Loop for printing count down timer
        notified = False
        notified2 = False
        while wait_time > 0:
            # Clear the console
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # Calculate hours and minutes to print
            minutes, seconds = divmod(int(wait_time), 60)
            hours, minutes = divmod(minutes, 60)

            # Print out time remaining
            print(f"<< {program_name} >>Time remaining until {target_time}: {hours:02d}:{minutes:02d}:00")
            
            # Notify 15 minutes before closing
            if not notified and wait_time <= 900:  
                self.notification.send_notification(f"<< {program_name} >> will close in 15 minutes.")
                notified = True

            # Notify 2 minutes before closing
            if not notified2 and wait_time <= 120:  
                self.notification.send_notification(f"<< {program_name} >> will close in 2 minutes.")
                notified2 = True
            
            # Minus wait_time
            time.sleep(60)
            wait_time -= 60

        # # Clear the console
        # os.system('cls' if os.name == 'nt' else 'clear')  