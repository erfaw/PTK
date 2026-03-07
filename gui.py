from tkinter import *
from tkinter import messagebox
from pathlib import Path

class Gui:
    def __init__(self):
        self.root = Tk()
        self.base_font = ('Calibri', 18, 'normal')
        self.font_path = Path(__file__).resolve().parent / 'fonts'

    def init_configs(self):
        self.root.title("P-T-K")
        self.root.minsize(50,50)
        # self.root.resizable(False, False)
        self.root.config(bg= "gray", padx=10, pady=10)

        self.titr_label_1 = Label(text= "Enter name of the program:", font= self.base_font, bg= "gray")
        self.titr_label_1.grid()

        self.program_name_entry = Entry(
            width= 30,
            font= self.base_font
        )
        self.program_name_entry.focus()
        self.program_name_entry.grid()

        self.titr_label_2 = Label(text= "Enter target time (e.g., 11:00 PM): ", font= self.base_font, bg= "gray")
        self.titr_label_2.grid()

        self.target_time_entry = Entry(
            width= 30,
            font= self.base_font
        )
        self.target_time_entry.grid(pady=10)

        self.accept_btn = Button(text= "Agree", width= 51)
    
    def accept_btn_clicked(self):
        self.program_name = self.program_name_entry.get().strip()
        self.target_time = self.target_time_entry.get().strip()
    
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
    
    # TODO : make a container which shows a progress bar or timer on top of first page with a 'cancele' btn
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

        self.timer_cancele_btn = Button(
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
        self.target_time_entry.grid_remove()
        self.accept_btn.grid_remove()
    
    def back_home(self):
        self.titr_label_1.grid()
        self.program_name_entry.grid()
        self.titr_label_2.grid()
        self.target_time_entry.grid()
        self.accept_btn.grid()

        self.timer_container.grid_remove()
        self.timer_cancele_btn.grid_remove()
    
    def update_timer_text(self, time_str):
        self.timer_container.itemconfig(
            self.time,
            text= time_str
        )

