from tkinter import *
from tkinter import messagebox
from pathlib import Path
from tkinter.ttk import Progressbar

class Gui:
    def __init__(self):
        self.root = Tk()
        self.base_font = ('Calibri', 18, 'normal')
        self.font_path = Path(__file__).resolve().parent / 'fonts'

    def init_configs(self, now_time_obj):
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
            width= 25,
            font= self.base_font
        ) 
        self.program_name_entry.focus()
        self.program_name_entry.grid(
            row= 1,
            column= 0,
            columnspan= 5
        )
        self.browse_btn = Button(
            text='Browse',
            bg='white',
            highlightthickness= 0,
            font= ('Calibri', 13, 'normal'),
            # command= cancele timer and restart,
        )
        self.browse_btn.grid(
            row= 1,
            column= 5,
            columnspan= 1
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
        if now_time_obj.hour >= 12:
            self.am_or_pm.select_set(1)
        else: 
            self.am_or_pm.select_set(0)

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
    
    def show_timer(self, program_name):
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
                65,
                "bold")
        )

        self.details = self.timer_container.create_text(
            45,
            10,
            text= f"{program_name}",
            font= ('Calibri', 9, 'normal') ,
            fill= 'white',
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
        self.first_page_elements = [
            self.titr_label_1,
            self.program_name_entry,
            self.titr_label_2,
            self.target_hour_entry,
            self.cologn_sign,
            self.target_minute_entry,
            self.accept_btn,
            self.am_or_pm,
            self.browse_btn,
        ]
        for element in self.first_page_elements:
            element.grid_remove()
    
    def back_home(self):
        for element in self.first_page_elements:
            element.grid()

        self.timer_page_elements = [
            self.timer_container,
            self.timer_cancele_btn,
            self.progress_bar,
        ]
        for element in self.timer_page_elements:
            element.grid_remove()
        self.update_progress_bar(0)
    
    def update_timer_text(self, time_str):
        self.timer_container.itemconfig(
            self.time,
            text= time_str
        )
    
    def update_progress_bar(self, value):
        self.progress_bar['value'] = value

    def render_browse_page(self, app_show):
        self.choose_page = Tk()
        self.choose_page.title('Choose a Program...')
        self.choose_page.config(bg= 'gray')

        for index, app in app_show.iterrows():
            def btn_func(app_name):
                self.program_name_entry.insert(END, app_name['name'])
                self.choose_page.destroy()

            button = Button(
                master= self.choose_page,
                text= f"{app['name']}",
                bg= 'white',
                highlightthickness= 0,
                font= ('Calibri', 13, 'normal'),
                width= 50,
                command= lambda app=app: btn_func(app)
            )
            button.pack()

        self.choose_page.mainloop()
        
# TODO : some how change icon of program
