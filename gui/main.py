from tkinter import Button, Canvas, PhotoImage, Label, Tk, Text
import tkinter
import tkinter.messagebox as mb
from pip._internal.utils.misc import tabulate
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists

default_width = 1280
default_height = 720
default_font = 'Terminal'
default_resolution = f'{default_width}x{default_height}'
default_pg_login = 'postgres'
default_pg_passwd = 'postgress'
default_pg_host = 'localhost'
default_pg_port = '5432'
default_pg_db_name = 'temp'
pg_url = f'postgresql+psycopg2://' \
         f'{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/{default_pg_db_name}'
default_font_color = '#f6eade'             # 639
default_active_font_color = '#f6eade'      # 639
default_button_color = '#e65e56'           # cf0
default_active_button_color = '#716e6a'    # 9c0
default_button_bg_color = '#f6eade'        # 90c
default_info_win_color = '#f6eade'         # 93c
default_info_font_color = '#4a4a4a'        # 222
additional_color_1 = '#4a4a4a'             # 528
# postgresql connection
my_engine = 0
output_text = 'Hello, world!\n'


def connect_db():
    global my_engine
    my_engine = create_engine(pg_url)


def hello():
    msg = 'Hello, world!'
    mb.showinfo('Info', msg)


class App(Tk):
    def __init__(self):
        super().__init__()

        global my_engine
        global output_text
        self.buttons_list = []
        # background image
        self.filename = PhotoImage(file='./bg_im.gif')
        self.background_label = Label(self, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_background = Canvas(self, width=400, height=720,
                                        bg=default_button_bg_color, highlightthickness=0)
        self.button_background.create_line(5, 5, 395, 5, fill=additional_color_1, dash=(40, 40), width=5)
        self.button_background.create_line(395, 5, 395, 715, fill=additional_color_1, dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 395, 715, fill=additional_color_1, dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 5, 5, fill=additional_color_1, dash=(40, 40), width=5)

        self.create_db_button = Button(text='Create DB', command=self.create_my_database, width=30, height=3, font=default_font+' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.drop_db_button = Button(text='Drop DB', command=self.drop_my_database, width=30, height=3, font=default_font+' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.show_db_menu_button = Button(text='Show tables', command=self.show_db_menu, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b4 = Button(text='Button4', command=hello, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b5 = Button(text='Actions with DB', command=self.create_or_drop_db_menu, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b6 = Button(text='Button6', command=hello, width=12, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.go_to_main_menu_button = Button(text='Back', command=self.main_menu, width=12, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.show_processors_button = Button(text='Processors', command=self.select_proc, width=12, height=3,
                                             font=default_font + ' 20',
                                             background=default_button_color, foreground=default_font_color,
                                             activebackground=default_active_button_color,
                                             activeforeground=default_active_font_color, bd=5)
        self.show_motherboards_button = Button(text='Motherboards', command=self.select_motherboard, width = 12, height = 3,
                                                font = default_font + ' 20', background = default_button_color,
                                                foreground = default_font_color,
                                                activebackground = default_active_button_color,
                                                activeforeground = default_active_font_color, bd = 5)
        self.show_gpu_button = Button(text='Graphics card', command=self.select_gpu, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_ram_button = Button(text='RAM', command=self.select_ram, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_cooling_button = Button(text='Cooling', command=self.select_cooling, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_power_supply_button = Button(text='Power supply', command=self.select_power_supply, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_ssd_button = Button(text='SSD', command=self.select_ssd, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_hdd_button = Button(text='HDD', command=self.select_hdd, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_case_button = Button(text='Cases', command=self.select_case, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_order_button = Button(text='Orders', command=self.select_order, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)
        self.show_customer_button = Button(text='Customers', command=self.select_customer, width=12, height=3,
                                               font=default_font + ' 20', background=default_button_color,
                                               foreground=default_font_color,
                                               activebackground=default_active_button_color,
                                               activeforeground=default_active_font_color, bd=5)

        self.info_output = Label(width=83, height=20, font=default_font+' 20', text=f'{output_text}',
                                 foreground=default_info_font_color, background=default_info_win_color,
                                 borderwidth=5,  relief="ridge", anchor='nw')

    def select_proc(self):
        Session = sessionmaker(bind=my_engine)
        session = Session()
        data = session.query(func.return_proc()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Cores', 'Threads',
                   'Integrated GPU', 'TDP', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(tuple(el1[1:-1].split(',')))
        output_str = ''
        output = tabulate(output)
        for i in output[0]:
            output_str += i + '\n'
        self.place_output_window(output_str)

    def select_motherboard(self):
        Session = sessionmaker(bind=my_engine)
        session = Session()
        data = session.query(func.return_proc()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Chipset', 'RAM type',
                   'RAM slots', 'Form-factor', 'M.2 slots', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(tuple(el1[1:-1].split(',')))
        output_str = ''
        output = tabulate(output)
        for i in output[0]:
            output_str += i + '\n'
        self.place_output_window(output_str)

    def select_gpu(self):
        pass

    def select_ram(self):
        pass

    def select_cooling(self):
        pass

    def select_power_supply(self):
        pass

    def select_ssd(self):
        pass

    def select_hdd(self):
        pass

    def select_case(self):
        pass

    def select_order(self):
        pass

    def select_customer(self):
        pass

    def place_output_window(self, info):
        self.info_output = Text(width=105, height=20, bg=default_info_win_color,
                                fg=default_info_font_color, wrap=tkinter.WORD)
        self.info_output.insert(tkinter.INSERT, info)
        self.info_output.configure(state='disabled')
        #Label(width=83, height=20, font=default_font + ' 20', text=f'{info}',
        #     foreground=default_info_font_color, background=default_info_win_color,
        #    borderwidth=5, relief="ridge", anchor='nw')
        self.info_output.place(x=20, y=100)

    def main_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        # self.b1.place(x=930, y=20)
        # self.b2.place(x=930, y=120)
        self.show_db_menu_button.place(x=930, y=220)
        self.buttons_list.append(self.show_db_menu_button)
        self.b4.place(x=930, y=320)
        self.buttons_list.append(self.b4)
        self.b5.place(x=930, y=420)
        self.buttons_list.append(self.b5)
        self.b6.place(x=930, y=520)
        self.buttons_list.append(self.b6)
        # self.b7.place(x=1110, y=520)
        self.place_output_window('')
        self.button_background.place(x=880, y=0)

    def show_db_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.show_processors_button.place(x=930, y=20)
        self.buttons_list.append(self.show_processors_button)

        self.show_motherboards_button.place(x=1110, y=20)
        self.buttons_list.append(self.show_motherboards_button)

        self.show_gpu_button.place(x=930, y=120)
        self.buttons_list.append(self.show_gpu_button)

        self.show_ram_button.place(x=1110, y=120)
        self.buttons_list.append(self.show_ram_button)

        self.show_cooling_button.place(x=930, y=220)
        self.buttons_list.append(self.show_cooling_button)

        self.show_power_supply_button.place(x=1110, y=220)
        self.buttons_list.append(self.show_power_supply_button)

        self.show_ssd_button.place(x=930, y=320)
        self.buttons_list.append(self.show_ssd_button)

        self.show_hdd_button.place(x=1110, y=320)
        self.buttons_list.append(self.show_hdd_button)

        self.go_to_main_menu_button.place(x=1110, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)

    def create_or_drop_db_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.create_db_button.place(x=930, y=20)
        self.buttons_list.append(self.create_db_button)
        self.drop_db_button.place(x=930, y=120)
        self.buttons_list.append(self.drop_db_button)
        self.go_to_main_menu_button.place(x=1110, y=520)
        self.buttons_list.append(self.go_to_main_menu_button)

    def create_my_database(self):
        if not database_exists(my_engine.url):
            create_database(my_engine.url)
            self.place_output_window(f'Database {default_pg_db_name} was created.\n')
        else:
            self.place_output_window(f'Database {default_pg_db_name} already created.\n')

    def drop_my_database(self):
        if database_exists(my_engine.url):
            drop_database(my_engine.url)
            self.place_output_window(f'Database {default_pg_db_name} was dropped.\n')
        else:
            self.place_output_window(f'Database {default_pg_db_name} not exists.\n')


if __name__ == '__main__':
    connect_db()
    app = App()
    app.geometry(default_resolution + '+120+50')
    app.title("Database editor")
    app.resizable(width=False, height=False)
    app.main_menu()
    app.mainloop()

#querCall = '''
#CALL insert_into_processor(1101, 'Intel', 'Celeron G5905', 'LGA 1200', 2, 2, 'Intel UHD Graphics 610', 58, 3999, 10);
#'''
#engine = create_engine("postgresql+psycopg2://postgres:postgress@localhost:5432/temp")
#engine.connect()
#comands = open('sql_comands.txt', 'r')
#query = comands.readlines()
#engine.execute(querCall)
#drop_database(engine.url)
#print(engine.execute(func.lower(querCall)).scalar())

