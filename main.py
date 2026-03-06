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
        ui.info(f"Program will close at {target_time}. Waiting...")
    except ValueError:
        ui.error("Invalid time format. Please use the format 'HH:MM AM/PM'.")
    else:
        def count_down_timer(count): # TODO : show a progress bar or actual timer with ui 
            global timer_after_id
            if count > 0 :
                timer_after_id = ui.root.after(1000, count_down_timer, count-1 )
            else: 
                ui.root.after_cancel(timer_after_id)
                if program_manager.kill(program_name):
                    ui.info(f"<< {program_name} >> closed!")
                else:
                    ui.info(f"<{program_name}> not found.")
        count_down_timer(wait_time)

ui.init_configs()

ui.accept_btn.config(
    command= main
)
ui.accept_btn.grid()

ui.root.mainloop()
