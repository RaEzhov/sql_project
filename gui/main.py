from tkinter import Button, Canvas, PhotoImage, Label, Tk, Text, Toplevel, ttk
import tkinter
import tkinter.messagebox as mb

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists


default_pg_login = 'user'
default_pg_passwd = 'password'
default_pg_host = 'localhost'   # '109.184.67.136'
default_pg_port = '5432'
default_pg_db_name = 'pc_shop'
pg_url = f'postgresql://' \
         f'{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/{default_pg_db_name}'
# db_connected = f'Connection with {pg_url} is lost.'
db_connected = f'Connected to {pg_url}'
default_width = 1280
default_height = 720
default_button_font = ('JetBrains Mono', 13)
default_font = ('JetBrains Mono', 11)
default_resolution = f'{default_width}x{default_height}'
default_font_color = '#f6eade'             # 639
default_active_font_color = '#f6eade'      # 639
default_button_color = '#e65e56'           # cf0
default_active_button_color = '#716e6a'    # 9c0
default_button_bg_color = '#f6eade'        # 90c
default_info_win_color = '#f6eade'         # 93c
default_info_font_color = '#000'           # 222
additional_color_1 = '#4a4a4a'             # 528
# postgresql connection
my_engine = 0


def max_length(lst):
    max_len = [0]*len(lst[0])
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            max_len[j] = max(len(lst[i][j]), max_len[j])
    return max_len


def add_spaces(lst):
    max_len = max_length(lst)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            length = len(lst[i][j])
            lst[i][j] = lst[i][j] + ' ' * (max_len[j] - length + 1)


def connect_db():
    global my_engine
    my_engine = create_engine(pg_url)


def hello():
    msg = 'Hello, world!'
    mb.showinfo('Info', msg)


class About(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = Label(self, text="Это всплывающее окно")
        self.button = Button(self, text="Закрыть", command=self.destroy)

        self.label.pack(padx=20, pady=20)
        self.button.pack(pady=5, ipadx=2, ipady=2)

        self.loadimage = PhotoImage(file="button.png")
        self.roundedbutton = Button(self, image=self.loadimage, text='Some text', compound="center", font='arial',
                                    foreground=default_font_color)
        self.roundedbutton["border"] = "0"
        self.roundedbutton.place(x=0, y=0)


class App(Tk):
    def __init__(self):
        super().__init__()
        global my_engine
        self.buttons_list = []
        # background image
        self.button_image = PhotoImage(file='button.png')
        self.button_half_image = PhotoImage(file='button_half.png')
        self.filename = PhotoImage(file='./bg_im.gif')
        self.background_label = Label(self, image=self.filename)

        self.info_output = Text(font=default_font, width=154, height=20, bg=default_info_win_color,
                                fg=default_info_font_color, wrap=tkinter.WORD)

        self.button_background = Canvas(self, width=1280, height=270,
                                        bg=default_button_bg_color, highlightthickness=0)
        self.button_background.create_line(5, 5, 1275, 5, fill=additional_color_1, width=2)
        self.button_background.create_line(1275, 5, 1275, 265, fill=additional_color_1, width=2)
        self.button_background.create_line(1275, 265, 5, 265, fill=additional_color_1, width=2)
        self.button_background.create_line(5, 265, 5, 5, fill=additional_color_1, width=2)

        self.button_background.create_oval(25-5, 35 - 5, 25 + 5, 35 + 5, fill='#0f0', outline="")
        self.button_background.create_text(35, 35, anchor=tkinter.W, font=default_font, text=db_connected)

        self.create_db_button = Button(text='Create DB', image=self.button_image, compound='center',
                                       command=self.create_my_database, foreground=default_font_color, border=0,
                                       background=default_button_bg_color, activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.drop_db_button = Button(text='Drop DB', command=self.drop_my_database, image=self.button_image,
                                     compound='center', foreground=default_font_color, border=0,
                                     background=default_button_bg_color, activebackground=default_button_bg_color,
                                     activeforeground=default_active_font_color, font=default_button_font)
        self.show_db_menu_button = Button(text='Show tables', command=self.show_db_menu, image=self.button_image,
                                          compound='center', foreground=default_font_color, border=0,
                                          background=default_button_bg_color, activebackground=default_button_bg_color,
                                          activeforeground=default_active_font_color, font=default_button_font)
        self.new_order_button = Button(text='New order', command=self.show_new_order_menu, image=self.button_image,
                                       compound='center', foreground=default_font_color, border=0,
                                       background=default_button_bg_color, activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.actions_with_db_button = Button(text='Actions with DB', command=self.create_or_drop_db_menu,
                                             image=self.button_image, compound='center', foreground=default_font_color,
                                             border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.exit_button = Button(text='Exit', command=self.exit_from_gui, foreground=default_font_color,
                                  image=self.button_half_image, compound='center', border=0,
                                  background=default_button_bg_color, activebackground=default_button_bg_color,
                                  activeforeground=default_active_font_color, font=default_button_font)
        self.go_to_main_menu_button = Button(text='Back', command=self.main_menu, foreground=default_font_color,
                                             image=self.button_half_image, compound='center', border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.show_processors_button = Button(text='Processors', command=self.select_proc, foreground=default_font_color,
                                             image=self.button_half_image, compound='center', border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.show_motherboards_button = Button(text='Motherboards', command=self.select_motherboard,
                                               foreground=default_font_color, image=self.button_half_image,
                                               compound='center', border=0,
                                               background=default_button_bg_color,
                                               activebackground=default_button_bg_color,
                                               activeforeground=default_active_font_color, font=default_button_font)
        self.show_gpu_button = Button(text='Videocards', command=self.select_gpu, foreground=default_font_color,
                                      image=self.button_half_image, compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_ram_button = Button(text='RAM', command=self.select_ram, foreground=default_font_color,
                                      image=self.button_half_image, compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_cooling_button = Button(text='Cooling', command=self.select_cooling, foreground=default_font_color,
                                          image=self.button_half_image, compound='center', border=0,
                                          background=default_button_bg_color, activebackground=default_button_bg_color,
                                          activeforeground=default_active_font_color, font=default_button_font)
        self.show_power_supply_button = Button(text='Power supply', command=self.select_power_supply,
                                               foreground=default_font_color, image=self.button_half_image,
                                               compound='center', border=0,
                                               background=default_button_bg_color,
                                               activebackground=default_button_bg_color,
                                               activeforeground=default_active_font_color, font=default_button_font)
        self.show_ssd_button = Button(text='SSD', command=self.select_ssd, foreground=default_font_color,
                                      image=self.button_half_image, compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_hdd_button = Button(text='HDD', command=self.select_hdd, foreground=default_font_color,
                                      image=self.button_half_image, compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_case_button = Button(text='Cases', command=self.select_case, foreground=default_font_color,
                                       image=self.button_half_image, compound='center', border=0,
                                       background=default_button_bg_color, activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.show_order_button = Button(text='Orders', command=self.select_order, image=self.button_image,
                                        compound='center', foreground=default_font_color, border=0,
                                        background=default_button_bg_color, activebackground=default_button_bg_color,
                                        activeforeground=default_active_font_color, font=default_button_font)
        self.show_customer_button = Button(text='Customers', command=self.select_customer, image=self.button_image,
                                           compound='center', foreground=default_font_color, border=0,
                                           background=default_button_bg_color, activebackground=default_button_bg_color,
                                           activeforeground=default_active_font_color, font=default_button_font)

    def select_proc(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_proc()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Cores', 'Threads',
                   'Integrated GPU', 'TDP', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_motherboard(self):

        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_motherboard()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Chipset', 'RAM type',
                   'RAM slots', 'Form-factor', 'M.2 slots', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_gpu(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_gpu()).all()
        output = []
        columns = ['SKU', 'Chip', 'Brand', 'Model', 'Memory capacity', 'Memory type',
                   'Length', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_ram(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_ram()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Type', 'Capacity',
                   'Frequency', 'Modules', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_cooling(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_cool()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'TDP',
                   'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_power_supply(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_power_supply()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Power', 'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_ssd(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_ssd()).all()
        output = []
        columns = ['SKU',  'Brand', 'Model', 'Capacity', 'Form factor',
                   'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_hdd(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_hdd()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Capacity','Rotation speed', 'Form factor',
                   'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_case(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_case()).all()
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Form factor', 'GPU lengh',
                   'Price', 'Amount']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_order(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_order()).all()
        output = []
        columns = ['ID', 'Customer phone', 'Processor', 'Cooling', 'RAM', 'RAM amt',
                   'Motherboard', 'GPU', 'HDD', 'SSD', 'Power supply', 'Case', 'Commentaries', 'Status', 'Price']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_customer(self):
        _Session = sessionmaker(bind=my_engine)
        session = _Session()
        data = session.query(func.return_customer()).all()
        output = []
        columns = ['Phone',
                   'First name', 'Last name']
        output.append(columns)
        for el in data:
            for el1 in el:
                output.append(list(el1[1:-1].replace('"', '').split(',')))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def place_output_window(self, info):
        self.info_output = Text(font=default_font, width=154, height=20, bg=default_info_win_color,
                                fg=default_info_font_color, wrap=tkinter.WORD)
        self.info_output.insert(tkinter.INSERT, info)
        self.info_output.configure(state='disabled')
        self.info_output.place(x=20, y=30)

    def main_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        # self.b1.place(x=930, y=20)
        # self.b2.place(x=930, y=120)
        self.show_db_menu_button.place(x=20, y=520)
        self.buttons_list.append(self.show_db_menu_button)
        self.new_order_button.place(x=20, y=620)
        self.buttons_list.append(self.new_order_button)
        self.actions_with_db_button.place(x=355, y=520)
        self.buttons_list.append(self.actions_with_db_button)
        self.exit_button.place(x=1120, y=620)
        self.buttons_list.append(self.exit_button)
        # self.b7.place(x=1110, y=520)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place_output_window('')
        self.button_background.place(x=0, y=450)

    def exit_from_gui(self):
        self.destroy()

    def show_db_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.show_processors_button.place(x=20, y=520)
        self.buttons_list.append(self.show_processors_button)

        self.show_motherboards_button.place(x=175, y=520)
        self.buttons_list.append(self.show_motherboards_button)

        self.show_gpu_button.place(x=330, y=520)
        self.buttons_list.append(self.show_gpu_button)

        self.show_ram_button.place(x=485, y=520)
        self.buttons_list.append(self.show_ram_button)

        self.show_cooling_button.place(x=485, y=620)
        self.buttons_list.append(self.show_cooling_button)

        self.show_power_supply_button.place(x=20, y=620)
        self.buttons_list.append(self.show_power_supply_button)

        self.show_ssd_button.place(x=175, y=620)
        self.buttons_list.append(self.show_ssd_button)

        self.show_hdd_button.place(x=330, y=620)
        self.buttons_list.append(self.show_hdd_button)

        self.show_case_button.place(x=970, y=620)
        self.buttons_list.append(self.show_case_button)

        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)

        self.show_order_button.place(x=640, y=520)
        self.buttons_list.append(self.show_order_button)

        self.show_customer_button.place(x=640, y=620)
        self.buttons_list.append(self.show_customer_button)

    def create_or_drop_db_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.create_db_button.place(x=20, y=520)
        self.buttons_list.append(self.create_db_button)
        self.drop_db_button.place(x=20, y=620)
        self.buttons_list.append(self.drop_db_button)
        self.go_to_main_menu_button.place(x=1120, y=620)
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

    def new_order(self):
        pass

    def show_new_order_menu(self):
        pass
        # new buttons (coonfirm, cancel)
        # Comboboxes with parts on info_label


if __name__ == '__main__':
    connect_db()
    app = App()
    app.geometry(default_resolution + '+120+50')
    app.title("Database editor")
    app.resizable(width=False, height=False)
    app.main_menu()
    app.mainloop()
