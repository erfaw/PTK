import os
import time
import psutil
from datetime import datetime
import platform
from plyer import notification

if platform.system() == "Windows":
    from win10toast import ToastNotifier

def find_processes(name):
    """Find all process IDs (PIDs) of a given program by its name."""
    pids = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        if proc.info['name'] and name.lower() in proc.info['name'].lower():
            pids.append(proc.info['pid'])
    return pids

def close_programs(pids, program_name):
    """Close all programs using their PIDs."""
    for pid in pids:
        try:
            os.kill(pid, 9)  # Sends SIGKILL to terminate the process
            print(f"<< {program_name} >> with PID {pid} has been closed.")
        except Exception as e:
            print(f"Error closing program with PID {pid}: {e}")

def calculate_wait_time(target_time):
    """Calculate the number of seconds to wait until the target time."""
    now = datetime.now()
    target = datetime.strptime(target_time, "%I:%M %p").replace(year=now.year, month=now.month, day=now.day)
    if target < now:
        target = target.replace(day=now.day + 1)  # Adjust for next day
    return (target - now).total_seconds()

# def send_notification(message):
#     """Send a notification to the user."""
#     if platform.system() == "Windows":
#         toaster = ToastNotifier()
#         toaster.show_toast("Program Closer Notification", message, duration=10)
#     else:
#         print(f"NOTIFICATION: {message}")

def send_notification(message):
    """Send a notification to the user."""
    notification.notify(
        title="Program Closer Notification",
        message=message,
        timeout=30  # Duration in seconds
    )

def countdown_timer(wait_time, target_time, program_name):
    """Display a countdown timer until the target time."""
    notified = False
    notified2 = False
    while wait_time > 0:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        minutes, seconds = divmod(int(wait_time), 60)
        hours, minutes = divmod(minutes, 60)
        print(f"<< {program_name} >>Time remaining until {target_time}: {hours:02d}:{minutes:02d}:00")

        if not notified and wait_time <= 900:  # Notify 15 minutes before closing
            send_notification(f"<< {program_name} >> will close in 15 minutes.")
            notified = True

        if not notified2 and wait_time <= 120:  # Notify 2 minutes before closing
            send_notification(f"<< {program_name} >> will close in 2 minutes.")
            notified2 = True

        time.sleep(60)
        wait_time -= 60

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

def main():
    while True:
        program_name = input("Enter the name of the program to close (e.g., notepad.exe): ").strip()
        target_time = input("Enter the target time to close the program (e.g., 11:00 PM): ").strip()

        try:
            wait_time = calculate_wait_time(target_time)
            print(f"Program will close at {target_time}. Waiting...")
            countdown_timer(wait_time, target_time, program_name)

            pids = find_processes(program_name)
            if pids:
                close_programs(pids, program_name)
            else:
                print(f"Program '{program_name}' not found.")
        except ValueError:
            print("Invalid time format. Please use the format 'HH:MM AM/PM'.")

        repeat = input("Do you want to schedule another program to close? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
