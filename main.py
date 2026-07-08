from program import ProgramManager
from timer import Timer
from notification import Notification
from gui import Gui
# TODO : think about how we could do this procedure for more than 1 program, either in one page or separated pages
# TODO : think about how could we implement common times for set, like 15min after now or 1h or 3h or whatever
program_manager = ProgramManager()

notification = Notification()

timer = Timer()

ui = Gui()

def main():
    program_name = ui.program_name_entry.get().strip()
    if not '.exe' in program_name :
        program_name = f"{program_name}.exe"

    target_hour = ui.target_hour_entry.get()
    target_minute = ui.target_minute_entry.get()
    target_am_pm = ui.am_or_pm.get(ui.am_or_pm.curselection())
    target_time = f"{target_hour}:{target_minute} {target_am_pm}"

    try:
        wait_time = timer.calculate_wait_time(target_time)
        ui.info(f"Program will close at {target_time}. Waiting...")
    except ValueError:
        ui.error("Invalid time format. Please use the format 'HH:MM AM/PM'.")
    else:
        ui.remove_grid_first_page()
        ui.show_timer(program_name= program_name)
        def command_cancel_btn_func():
            ui.root.after_cancel(timer_after_id)
            ui.back_home()
            ui.info("Timer canceled...")
        ui.timer_cancele_btn.config(
            command= command_cancel_btn_func,
        )
        def count_down_timer(count):
            global timer_after_id
            if count > 0 :
                ui.update_timer_text(
                    timer.format_time(count)
                )
                ui.update_progress_bar(
                    (1-(count/wait_time))*100
                )
                if ui.is_notif_one_half_min.get() and int(count) == 1.5*60 :
                    notification.send(f"<< {program_name} >> will close in 1.5 minutes.")
                elif ui.is_notif_fifteen_min.get() and int(count) == 15*60 :
                    notification.send(f"<< {program_name} >> will close in 15 minutes.")
                timer_after_id = ui.root.after(
                    1000,
                    count_down_timer,
                    count-1,
                )
            else: 
                ui.root.after_cancel(timer_after_id)
                if program_manager.kill(program_name):
                    ui.info(f"<< {program_name} >> closed!")
                else:
                    ui.info(f"<{program_name}> not found.")
                ui.back_home()
        count_down_timer(wait_time)

def take_program_from_sys():
    ui.program_name_entry.delete(0, 'end')
    program_manager.df_client_apps = program_manager.get_open_programs()
    ui.render_browse_page(
        app_show = program_manager.df_client_apps.drop_duplicates('name')
    )

ui.init_configs(
    now_time_obj= timer.get_now()
)

ui.accept_btn.config(
    command= main
)

ui.browse_btn.config(
    command= take_program_from_sys
)

ui.root.mainloop()
