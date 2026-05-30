
# <img src="./icons/icon.ico" width=25px> PTK (Process-To-Kill) 
<!-- | [Screen Shots](https://github.com/erfaw/PTK#screen-shots) 
| -->
   ## 📝 Overview 
   This project is a **desktop application** built with `Python` & `Tkinter` that ***helps users limit the amount of time spent using specific programs***. 
   
   It was originally created as a `personal productivity tool` to reduce gaming time and encourage better time management.

   Users can either type a process name manually or select one through the built-in `Browse` feature. The application creates a `countdown timer`, `sends notification reminders` before the time expires, and `automatically terminates the selected process` when the timer reaches zero.

   **NOTE** : Currently, the application has only been tested on Windows and must be run with administrator privileges in order to manage and terminate external processes.

   ### Architecture

   I tried to project follows Object-Oriented Programming (OOP) principles and Separation of Concerns. Responsibilities are divided into dedicated Classes in separate modules:

   * **ProgramManager** – Process discovery, management, and termination.
   * **Timer** – Time calculations, formatting, and countdown management.
   * **Notification** – User notification delivery.
   * **GUI** – User interface, input handling, warnings, and timer visualization.

   These components are orchestrated by `main.py`, which acts as the application's entry point.

   ---

   ## ▶️ How to Run
   1. Ensure you have Python installed.

   2. Clone the repository: 
      ```
      git clone https://github.com/erfaw/PTK
      ```

   3. Make Virtual Environment: 
      ```
      python -m venv .venv
      ```

      then on Git Bash: 
      ```
      source ./.venv/Scripts/activate
      ```

   4. Install dependencies: 
      ```
      pip install -r requirements.txt
      ```

   5. Run : 
      ```
      python main.py
      ```

   ---

   ## 🌟 Features

   * Set a `custom time limit` for any running application.
   * `Select a target program` by entering its `process name` or using the `Browse feature`.
   * Display a `live countdown timer` until the selected application is terminated.
   * Send `reminder notifications` <u>15 minutes</u> and <u>1.5 minutes</u> before the time limit expires.
   * Automatically `terminate` the target process when the timer reaches zero.
   * `Filter unrelated processes` from the `Browse list` to simplify program selection.
   * Designed and tested for `Windows` environments.
   * `Need administrator privileges` for managing external processes.


   ---

   ## 🖼️ Preview

   ---

   ## 💡 What I Learned 
