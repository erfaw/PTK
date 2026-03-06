from program import ProgramManager
from timer import Timer
from notification import Notification
import os
from gui import Gui

program_manager = ProgramManager()

notification = Notification()

timer = Timer(notif_obj= notification)

ui = Gui()

def main():
    program_name = input("Enter the name of the program to close (e.g., notepad.exe): ").strip()

    target_time = input("Enter the target time to close the program (e.g., 11:00 PM): ").strip()

    try:
        wait_time = timer.calculate_wait_time(target_time)
        print(f"Program will close at {target_time}. Waiting...")

        timer.countdown_timer(wait_time, target_time, program_name)

        pids = program_manager.find_processes(program_name)
        if pids:
            program_manager.close_programs(pids, program_name)
        else:
            print(f"Program '{program_name}' not found.")

    except ValueError:
        print("Invalid time format. Please use the format 'HH:MM AM/PM'.")

    repeat = input("Do you want to schedule another program to close? ([Y]es/[N]o): ").strip().lower()
    if repeat != 'y':
        print("Exiting the program.")

ui.init_configs()

ui.accept_btn.config(
    command= main
)
ui.accept_btn.grid()

ui.root.mainloop()
