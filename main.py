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
    program_name = ui.program_name_entry.get().strip()

    target_time = ui.target_time_entry.get().strip()

    input(f"program_name:\t{program_name}\ntarget_time:\t{target_time}")

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
