from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        self.base_font = ('Calibri', 18, 'normal')
        self.title("P-T-K")
        self.minsize(50,50)
        # self.resizable(False, False)
        self.config(bg= "gray", padx=10, pady=10)

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

        self.accept_btn = Button(text= "Agree", width= 51, command= self.accept_btn_clicked)
        self.accept_btn.grid()
    
    def accept_btn_clicked(self):
        self.program_name = self.program_name_entry.get().strip()
        self.target_time = self.target_time_entry.get().strip()
