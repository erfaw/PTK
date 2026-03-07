from tkinter import *
from tkinter import messagebox
from pathlib import Path
from tkinter.ttk import Progressbar

class Gui:
    def __init__(self):
        self.root = Tk()
        self.base_font = ('Calibri', 18, 'normal')
        self.font_path = Path(__file__).resolve().parent / 'fonts'

    def init_configs(self):
        self.root.title("P-T-K")
        self.root.minsize(50,50)
        self.root.resizable(False, False)
        self.root.config(bg= "gray", padx=10, pady=10)

        self.titr_label_1 = Label(
            text= "Enter name of the program:",
            font= self.base_font,
            bg= "gray",
            anchor= 'w',
            width= 30,
        )
        self.titr_label_1.grid(
            row=0,
            column= 0,
            columnspan= 6,
        )

        self.program_name_entry = Entry(
            width= 30,
            font= self.base_font
        ) # TODO : alongside of entry, build a btn to render a page, which had a list of open programs from taskbar of system for user to choose (instead of type program name itself) 
        self.program_name_entry.focus()
        self.program_name_entry.grid(
            row= 1,
            column= 0,
            columnspan= 6
        )

        self.titr_label_2 = Label(
            text= "Enter target time (e.g., 11:00 PM): ",
            font= self.base_font,
            bg= "gray",
            anchor= 'w',
            width= 30,
        )
        self.titr_label_2.grid(
            row= 2,
            column= 0,
            columnspan= 6
        )

        self.target_hour_entry = Spinbox(
            from_=1,
            to=12,
            width=10,
            font= self.base_font,
            justify= 'center',
            # command=None
        )
        self.cologn_sign = Label(
            text=' : ',
            bg= "gray",
            font= self.base_font    
        )
        self.target_minute_entry = Spinbox(
            from_=0,
            to=59,
            width=10,
            font= self.base_font,
            justify= 'center',
            # command=None
        )
        self.target_hour_entry.grid(
            row= 3,
            column= 0,
            columnspan= 2,
        )
        self.cologn_sign.grid(
            row= 3,
            column= 2,
            columnspan= 1,
        )
        self.target_minute_entry.grid(
            row= 3,
            column= 3,
            columnspan= 2,
        )
        self.am_or_pm = Listbox(height= 2, width=5)
        am_pm = ['AM', 'PM']
        for _ in am_pm:
            self.am_or_pm.insert(am_pm.index(_), _)
        self.am_or_pm.grid(
            row= 3,
            column= 5,
        )

        self.accept_btn = Button(text= "Agree", width= 51)
        self.accept_btn.grid(
            pady= 2,
            row= 4,
            column= 0,
            columnspan= 6
        )
    
    def warn(self, message):
        messagebox.showwarning(
            message= message
        )

    def info(self, message):
        messagebox.showinfo(
            message= message
        )

    def error(self, message):
        messagebox.showerror(
            message= message
        )
    
    def show_timer(self):
        self.timer_container = Canvas(
            self.root,
            bg= 'black',
            width= self.root.winfo_width(),
            height= self.root.winfo_height()//2
        )
        self.timer_container.grid(
            row=0
        )

        # TODO : render a text to show this timer is for what program
        self.time = self.timer_container.create_text(
            200,
            60,
            text= '00:00',
            fill= 'white',
            font= (
                self.font_path/'SOURCECODEPRO-REGULAR.TTF',
                90,
                "bold")
        )

        self.progress_bar = Progressbar(
            self.root,
            orient= HORIZONTAL,
            length= self.root.winfo_width(),
            mode='determinate'
        )
        self.progress_bar.grid(pady=2)

        self.timer_cancele_btn = Button( # TODO : choose a better color for this btn
            text='Cancel',
            bg='red',
            highlightthickness= 0,
            # command= cancele timer and restart,
            width= 55
        )
        self.timer_cancele_btn.grid()

    def remove_grid_first_page(self):
        self.titr_label_1.grid_remove()
        self.program_name_entry.grid_remove()
        self.titr_label_2.grid_remove()
        self.target_hour_entry.grid_remove()
        self.cologn_sign.grid_remove()
        self.target_minute_entry.grid_remove()
        self.accept_btn.grid_remove()
        self.am_or_pm.grid_remove()
    
    def back_home(self):
        self.titr_label_1.grid()
        self.program_name_entry.grid()
        self.titr_label_2.grid()
        self.target_hour_entry.grid()
        self.cologn_sign.grid()
        self.target_minute_entry.grid()
        self.accept_btn.grid()
        self.am_or_pm.grid()

        self.timer_container.grid_remove()
        self.timer_cancele_btn.grid_remove()
        self.update_progress_bar(0)
        self.progress_bar.grid_remove()
    
    def update_timer_text(self, time_str):
        self.timer_container.itemconfig(
            self.time,
            text= time_str
        )
    
    def update_progress_bar(self, value):
        self.progress_bar['value'] = value

# TODO : some how change icon of program
