from program import ProgramManager
from timer import Timer
from notification import Notification
import os
from gui import Gui

# Build an object from Program Manager to operate with programs
program_manager = ProgramManager()

# Build an object from Notification to use in other objects
notification = Notification()

# Build an object from Timer to take care of time things
timer = Timer(notif_obj= notification)

# Build an object from Gui to take care of graphic interface
ui = Gui()

# main function to make program repeatable
def main():
    while True:
        # Clear screen before start
        os.system('cls' if os.name == 'nt' else 'clear')

        # Ask about program name
        program_name = input("Enter the name of the program to close (e.g., notepad.exe): ").strip()

        # Ask about target time to close program
        target_time = input("Enter the target time to close the program (e.g., 11:00 PM): ").strip()

        # Calculate and set timer to close
        try:
            wait_time = timer.calculate_wait_time(target_time)
            print(f"Program will close at {target_time}. Waiting...")

            # Run countdown timer
            timer.countdown_timer(wait_time, target_time, program_name)

            # Closing program
            pids = program_manager.find_processes(program_name)
            if pids:
                program_manager.close_programs(pids, program_name)
            else:
                print(f"Program '{program_name}' not found.")

        # Catch exception when user input wrong time to target
        except ValueError:
            print("Invalid time format. Please use the format 'HH:MM AM/PM'.")

        # Ask about Repeat
        repeat = input("Do you want to schedule another program to close? ([Y]es/[N]o): ").strip().lower()
        if repeat != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()