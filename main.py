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

    try:
        wait_time = timer.calculate_wait_time(target_time)
        print(f"Program will close at {target_time}. Waiting...")

        timer_after_id = None
        def count_down_timer(count):
            global timer_after_id
            print(f"last:\t{count}")
            if count > 0 :
                timer_after_id = ui.root.after(1000, count_down_timer, count-1 )
            else: 
                ui.root.after_cancel(timer_after_id)
                program_manager.kill(program_name= program_name)
        count_down_timer(wait_time)

    except ValueError: # TODO : check if you can do it just for wait_time initialization line and do the rest in 'else' of try-except statement
        print("Invalid time format. Please use the format 'HH:MM AM/PM'.")

ui.init_configs()

ui.accept_btn.config(
    command= main
)
ui.accept_btn.grid()

ui.root.mainloop()
