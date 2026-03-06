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
    program_name = input("Enter the name of the program to close (e.g., notepad.exe): ").strip() # TODO : get it from ui

    target_time = input("Enter the target time to close the program (e.g., 11:00 PM): ").strip() # TODO : get it from ui

    try:
        wait_time = timer.calculate_wait_time(target_time)
        print(f"Program will close at {target_time}. Waiting...")

        timer.countdown_timer(wait_time, target_time, program_name) # TODO : need change with a better way

        pids = program_manager.find_processes(program_name) # TODO : make whole this part a function named 'kill'
        if pids:
            program_manager.close_programs(pids, program_name)
        else:
            print(f"Program '{program_name}' not found.")
    except ValueError: # TODO : check if you can do it just for wait_time initialization line and do the rest in 'else' of try-except statement
        print("Invalid time format. Please use the format 'HH:MM AM/PM'.")

ui.init_configs()

ui.accept_btn.config(
    command= main
)
ui.accept_btn.grid()

ui.root.mainloop()
