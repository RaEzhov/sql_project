from tkinter import Button, Canvas, PhotoImage, Label, Tk, Text, Entry, Checkbutton, ttk
import tkinter
import tkinter.messagebox as mb

from sqlalchemy import create_engine

default_pg_login = 'user'
default_pg_passwd = 'password'
default_pg_host = 'localhost'
default_pg_port = '5432'
default_pg_db_name = 'pc_shop'
pg_url = f'postgresql://' \
         f'{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/{default_pg_db_name}'
god_url = f'postgresql://' \
         f'{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/god'
db_connected = f'Connected to {pg_url}'
db_not_connected = f'Connection with {pg_url} is lost.'
default_width = 1280
default_height = 720
default_button_font = ('JetBrains Mono', 13)
default_font = ('JetBrains Mono', 11)
default_resolution = f'{default_width}x{default_height}'
default_font_color = '#f6eade'
default_active_font_color = '#f6eade'
default_button_color = '#e65e56'
default_active_button_color = '#716e6a'
default_button_bg_color = '#f6eade'
default_info_win_color = '#f6eade'
default_info_font_color = '#000'
additional_color_1 = '#4a4a4a'
god_engine = 0
god_cursor = 0
is_exists = 1
my_engine = 0
my_cursor = 0
motherboard_form_factor_dict = {'Mini-ITX': 0,
                                'Micro-ATX': 1,
                                'Mini-ATX': 2,
                                'Standart-ATX': 3,
                                'XL-ATX': 4,
                                'E-ATX': 5}
names_of_tables = ['proc', 'motherboard', 'gpu', 'ram', 'cool', 'power_supply', 'ssd', 'hdd', 'case_pc']
other_tables = ['order_customer', 'customer']


def update_is_exists():
    global is_exists
    res_exec = god_cursor.execute('''SELECT * FROM is_exists();''')
    for res_select in res_exec:
        is_exists = res_select[0]


def max_length(lst):
    max_len = [0]*len(lst[0])
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            max_len[j] = max(len(str(lst[i][j])), max_len[j])
    return max_len


def add_spaces(lst):
    max_len = max_length(lst)
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            length = len(str(lst[i][j]))
            lst[i][j] = str(lst[i][j]) + ' ' * (max_len[j] - length + 1)


def make_list_of_str(lst):
    for i in range(len(lst)):
        tmp_str = ''
        for j in range(len(lst[i])):
            tmp_str += str(lst[i][j]) + ' '
        lst[i] = tmp_str


def connect_db():
    global my_engine, my_cursor
    my_engine = create_engine(pg_url)
    my_cursor = my_engine.connect()


def disconnect_db():
    global my_engine, my_cursor
    my_cursor.close()
    my_engine.dispose()


def validate(new_value):
    return new_value == "" or new_value.isnumeric()


class App(Tk):
    def __init__(self):
        super().__init__()
        global my_engine
        self.buttons_list = []
        self.button_image = PhotoImage(file='button.png')
        self.button_half_image = PhotoImage(file='button_half.png')
        self.filename = PhotoImage(file='./bg_im.gif')
        self.background_label = Label(self, image=self.filename)

        self.info_output = 0
        self.combo_boxes = []
        self.checkbox_values = []
        self.components_dict = {}
        self.button_background = Canvas(self, width=1280, height=270,
                                        bg=default_button_bg_color, highlightthickness=0)
        self.sku_entry = Entry(font=default_font, background=additional_color_1, foreground=default_info_win_color,
                               width=4)
        self.customer_phone_entry = Entry(font=default_font, background=additional_color_1,
                                          foreground=default_info_win_color, width=11)
        self.customer_phone_text = Text(font=default_font, width=15, height=1, bg=default_info_win_color,
                                        fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.sku_text = Text(font=default_font, width=4, height=1, bg=default_info_win_color,
                             fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.button_background.create_line(5, 5, 1275, 5, fill=additional_color_1, width=2)
        self.button_background.create_line(1275, 5, 1275, 265, fill=additional_color_1, width=2)
        self.button_background.create_line(1275, 265, 5, 265, fill=additional_color_1, width=2)
        self.button_background.create_line(5, 265, 5, 5, fill=additional_color_1, width=2)

        self.status_point = self.button_background.create_oval(25 - 5, 35 - 5, 25 + 5, 35 + 5, fill='#f00',
                                                               outline="")
        self.status_text = self.button_background.create_text(35, 35, anchor=tkinter.W, font=default_font,
                                                              text=db_not_connected)

        self.create_db_button = Button(text='Create DB', image=self.button_image, compound='center',
                                       command=self.create_my_database, foreground=default_font_color, border=0,
                                       background=default_button_bg_color, activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.drop_db_button = Button(text='Drop DB', command=self.drop_my_database, image=self.button_image,
                                     compound='center', foreground=default_font_color, border=0,
                                     background=default_button_bg_color, activebackground=default_button_bg_color,
                                     activeforeground=default_active_font_color, font=default_button_font)
        self.show_db_menu_button = Button(text='Show tables and SKU search', command=self.show_db_menu,
                                          image=self.button_image, compound='center',
                                          foreground=default_font_color, border=0,
                                          background=default_button_bg_color,
                                          activebackground=default_button_bg_color,
                                          activeforeground=default_active_font_color, font=default_button_font)
        self.new_order_button = Button(text='New order', command=self.show_new_order_menu, image=self.button_image,
                                       compound='center', foreground=default_font_color, border=0,
                                       background=default_button_bg_color, activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.actions_with_db_button = Button(text='Actions with DB', command=self.create_or_drop_db_menu,
                                             image=self.button_image, compound='center',
                                             foreground=default_font_color,
                                             border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.clearing_tables_button = Button(text='Clear tables', command=self.clear_tables_menu,
                                             image=self.button_image, compound='center',
                                             foreground=default_font_color,
                                             border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.clear_chosen_tables_button = Button(text='Clear chosen tables', command=self.clear_chosen_tables,
                                                 image=self.button_image, compound='center',
                                                 foreground=default_font_color, border=0,
                                                 background=default_button_bg_color,
                                                 activebackground=default_button_bg_color,
                                                 activeforeground=default_active_font_color,
                                                 font=default_button_font)
        self.clear_all_tables_button = Button(text='Clear all tables', command=self.clear_all_tables,
                                              image=self.button_image, compound='center',
                                              foreground=default_font_color, border=0,
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
        self.show_processors_button = Button(text='Processors', command=self.select_proc,
                                             foreground=default_font_color,
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
        self.show_gpu_button = Button(text='Graphics\ncards', command=self.select_gpu,
                                      foreground=default_font_color, image=self.button_half_image,
                                      compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_ram_button = Button(text='RAM', command=self.select_ram, foreground=default_font_color,
                                      image=self.button_half_image, compound='center', border=0,
                                      background=default_button_bg_color, activebackground=default_button_bg_color,
                                      activeforeground=default_active_font_color, font=default_button_font)
        self.show_cooling_button = Button(text='Cooling', command=self.select_cooling,
                                          foreground=default_font_color,
                                          image=self.button_half_image, compound='center', border=0,
                                          background=default_button_bg_color,
                                          activebackground=default_button_bg_color,
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
                                        background=default_button_bg_color,
                                        activebackground=default_button_bg_color,
                                        activeforeground=default_active_font_color, font=default_button_font)
        self.show_customer_button = Button(text='Customers', command=self.select_customer, image=self.button_image,
                                           compound='center', foreground=default_font_color, border=0,
                                           background=default_button_bg_color,
                                           activebackground=default_button_bg_color,
                                           activeforeground=default_active_font_color, font=default_button_font)
        self.confirm_order_button = Button(text='Confirm', command=self.new_order,
                                           image=self.button_image, compound='center',
                                           foreground=default_font_color, border=0,
                                           background=default_button_bg_color,
                                           activebackground=default_button_bg_color,
                                           activeforeground=default_active_font_color, font=default_button_font)
        self.sku_search_button = Button(text='SKU search', command=self.sku_search,
                                        image=self.button_image, compound='center',
                                        foreground=default_font_color, border=0,
                                        background=default_button_bg_color,
                                        activebackground=default_button_bg_color,
                                        activeforeground=default_active_font_color, font=default_button_font)

    def select_proc(self):
        data = my_cursor.execute(f'''SELECT * FROM return_proc();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Cores', 'Threads',
                   'Integrated GPU', 'TDP', 'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_motherboard(self):
        data = my_cursor.execute(f'''SELECT * FROM return_motherboard();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'Chipset', 'RAM type',
                   'RAM slots', 'Form-factor', 'M.2 slots', 'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_gpu(self):
        data = my_cursor.execute(f'''SELECT * FROM return_gpu();''')
        output = []
        columns = ['SKU', 'Chip', 'Brand', 'Model', 'Memory capacity', 'Memory type',
                   'Length', 'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_ram(self):
        data = my_cursor.execute(f'''SELECT * FROM return_ram();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Type', 'Capacity',
                   'Frequency', 'Modules', 'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_cooling(self):
        data = my_cursor.execute(f'''SELECT * FROM return_cool();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Socket', 'TDP',
                   'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_power_supply(self):
        data = my_cursor.execute(f'''SELECT * FROM return_power_supply();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Power', 'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_ssd(self):
        data = my_cursor.execute(f'''SELECT * FROM return_ssd();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Capacity', 'Form factor',
                   'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_hdd(self):
        data = my_cursor.execute(f'''SELECT * FROM return_hdd();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Capacity', 'Rotation speed', 'Form factor',
                   'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_case(self):
        data = my_cursor.execute(f'''SELECT * FROM return_case_pc();''')
        output = []
        columns = ['SKU', 'Brand', 'Model', 'Form factor', 'GPU lengh',
                   'Price', 'Amount']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_order(self):
        data = my_cursor.execute(f'''SELECT * FROM return_order_customer();''')
        output = []
        columns = ['ID', 'Customer', 'CPU', 'Cooling', 'RAM', 'RAM amt',
                   'MoBo', 'GPU', 'HDD', 'SSD', 'PSU', 'Case', 'Commentaries', 'Status', 'Price']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def select_customer(self):
        data = my_cursor.execute(f'''SELECT * FROM return_customer();''')
        output = []
        columns = ['Phone', 'First name', 'Last name']
        output.append(columns)
        for i in data:
            output.append(list(i))
        output_str = ''
        add_spaces(output)
        for i in output:
            for j in i:
                output_str += j + '|'
            output_str += '\n'
        self.place_output_window(output_str)

    def place_output_window(self, info):
        self.info_output = Text(font=default_font, width=137, height=20, bg=default_info_win_color,
                                fg=default_info_font_color, wrap=tkinter.WORD)
        self.info_output.insert(tkinter.INSERT, info)
        self.info_output.configure(state='disabled')
        self.info_output.place(x=20, y=30)

    def update_connection_status(self):
        self.button_background.delete(self.status_point)
        self.button_background.delete(self.status_text)
        if is_exists == 1:
            self.status_point = self.button_background.create_oval(25 - 5, 35 - 5, 25 + 5, 35 + 5, fill='#f00',
                                                                   outline="")
            self.status_text = self.button_background.create_text(35, 35, anchor=tkinter.W, font=default_font,
                                                                  text=db_not_connected)
        else:
            self.status_point = self.button_background.create_oval(25 - 5, 35 - 5, 25 + 5, 35 + 5, fill='#0f0',
                                                                   outline="")
            self.status_text = self.button_background.create_text(35, 35, anchor=tkinter.W, font=default_font,
                                                                  text=db_connected)

    def main_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        update_is_exists()
        self.update_connection_status()
        if is_exists == 1:
            self.new_order_button['state'] = 'disabled'
            self.show_db_menu_button['state'] = 'disabled'
            self.clearing_tables_button['state'] = 'disabled'
        else:
            self.new_order_button['state'] = 'normal'
            self.show_db_menu_button['state'] = 'normal'
            self.clearing_tables_button['state'] = 'normal'
        self.show_db_menu_button.place(x=20, y=520)
        self.buttons_list.append(self.show_db_menu_button)
        self.new_order_button.place(x=20, y=620)
        self.buttons_list.append(self.new_order_button)
        self.actions_with_db_button.place(x=340, y=520)
        self.buttons_list.append(self.actions_with_db_button)
        self.clearing_tables_button.place(x=340, y=620)
        self.buttons_list.append(self.clearing_tables_button)
        self.exit_button.place(x=1120, y=620)
        self.buttons_list.append(self.exit_button)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place_output_window('')
        self.button_background.place(x=0, y=450)

    def clear_tables_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.clear_chosen_tables_button.place(x=20, y=520)
        self.buttons_list.append(self.clear_chosen_tables_button)
        self.clear_all_tables_button.place(x=20, y=620)
        self.buttons_list.append(self.clear_all_tables_button)
        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)
        self.checkbox_values = [tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(),
                                tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar(),
                                tkinter.IntVar(), tkinter.IntVar(), tkinter.IntVar()
                                ]
        checkbox_list = [Checkbutton(text='Processor', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[0], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='Motherboard', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[1], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='Graphics card', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[2], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='RAM', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[3], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='Cooling', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[4], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='Power supply', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[5], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='SSD', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[6], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='HDD', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[7], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         Checkbutton(text='Case', font=default_font, background=default_button_bg_color,
                                     variable=self.checkbox_values[8], activebackground=default_button_bg_color,
                                     onvalue=1, offvalue=0),
                         ]
        for i in range(9):
            checkbox_list[i].place(x=30, y=i*40 + 40)

    def clear_chosen_tables(self):
        for i in range(9):
            table = self.checkbox_values[i].get()
            if table == 1:
                query = f'CALL clear_{names_of_tables[i]}();'
                my_cursor.execute(query)

    def clear_all_tables(self):
        self.place_output_window('All tables was cleared.')
        query = f'''CALL clear_all_tables();'''
        my_cursor.execute(query)

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

    def show_new_order_menu(self):
        self.place_output_window(' Choose components:\n\n Processor\n\n Motherboard\n\n Graphics card\n\n RAM\t\t\t\t\t'
                                 '\t\t\t\t\t\t\t\t\t\t\t(amount)\n\n Cooling\n\n Power supply\n\n SSD\n\n HDD\n\n Case')
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []

        self.confirm_order_button.place(x=20, y=520)
        self.buttons_list.append(self.confirm_order_button)

        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)

        self.customer_phone_text.insert(tkinter.INSERT, 'Customer phone:')
        self.customer_phone_text.configure(state='disabled')
        self.customer_phone_text.place(x=1008, y=481)
        self.buttons_list.append(self.customer_phone_text)

        self.customer_phone_entry.place(x=1150, y=480)
        self.buttons_list.append(self.customer_phone_entry)

        self.combo_boxes = []
        self.components_dict = {}
        for i in range(9):
            data = my_cursor.execute(f'''SELECT * FROM return_{names_of_tables[i]}();''')
            output = []
            for el in data:
                value = list(el)
                output.append(value)
                self.components_dict[value[0]] = value
            make_list_of_str(output)
            self.combo_boxes.append(ttk.Combobox(self, font=default_font, values=output, width=106, state='readonly'))
            self.combo_boxes[i].place(x=150, y=68 + i*38)
        vcmd = (self.register(validate), '%P')
        ram_amount = Entry(self, font=default_font, width=3, validate='key', validatecommand=vcmd)
        self.combo_boxes.append(ram_amount)
        ram_amount.place(x=1140, y=183)

    def sku_search(self):
        sku = self.sku_entry.get()
        if len(sku) != 4 or not sku.isdecimal() or sku[0] == '0':
            mb.showinfo('Information', message='SKU is not supported!')
        else:
            query = f'''SELECT * FROM find_{names_of_tables[int(sku[0]) - 1]}_with_sku({sku});'''
            res = my_cursor.execute(query)
            res_str = ''
            for i in res:
                for j in i:
                    res_str += str(j) + '\t'
            if res_str:
                self.place_output_window(res_str)
            else:
                self.place_output_window('SKU not found!')

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

        self.show_case_button.place(x=960, y=620)
        self.buttons_list.append(self.show_case_button)

        self.show_order_button.place(x=640, y=520)
        self.buttons_list.append(self.show_order_button)

        self.show_customer_button.place(x=640, y=620)
        self.buttons_list.append(self.show_customer_button)

        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)

        self.sku_search_button.place(x=960, y=520)
        self.buttons_list.append(self.sku_search_button)

        self.sku_entry.place(x=1175, y=495)
        self.buttons_list.append(self.sku_entry)

        self.sku_text.insert(tkinter.INSERT, 'SKU:')
        self.sku_text.configure(state='disabled')
        self.sku_text.place(x=1135, y=497)
        self.buttons_list.append(self.sku_text)

    def create_my_database(self):
        global is_exists
        if is_exists == 1:
            god_cursor.execute(f'''SELECT create_db();''')
            connect_db()
            self.place_output_window(f'Database {default_pg_db_name} was created.\n')
            update_is_exists()
            self.update_connection_status()
        else:
            self.place_output_window(f'Database {default_pg_db_name} already created.\n')

    def drop_my_database(self):
        if is_exists == 0:
            disconnect_db()
            god_cursor.execute(f'''SELECT drop_db();''')
            self.place_output_window(f'Database {default_pg_db_name} was dropped.\n')
            update_is_exists()
            self.update_connection_status()
        else:
            self.place_output_window(f'Database {default_pg_db_name} not exists.\n')

    def new_order(self):
        sku_list = []
        for i in range(10):
            sku_list.append(int(self.combo_boxes[i].get()[0:4]))
        customer_number = self.customer_phone_entry.get()
        if len(customer_number) != 11 or not customer_number.isdigit():
            mb.showinfo('Information', message='Customer phone number is not supported!')
        elif '' in sku_list:
            mb.showinfo('Information', message='Not all components selected!')
        elif self.components_dict[sku_list[0]][3] != self.components_dict[sku_list[1]][3] or \
                self.components_dict[sku_list[3]][3] != self.components_dict[sku_list[1]][5] or \
                self.components_dict[sku_list[1]][6] < sku_list[9] * self.components_dict[sku_list[3]][6] or \
                self.components_dict[sku_list[6]][4] == 'm.2' and self.components_dict[sku_list[1]][8] == '0' or \
                motherboard_form_factor_dict[self.components_dict[sku_list[1]][7]] > \
                motherboard_form_factor_dict[self.components_dict[sku_list[8]][3]] or \
                self.components_dict[sku_list[2]][6] > self.components_dict[sku_list[8]][4] or \
                self.components_dict[sku_list[4]][3] != self.components_dict[sku_list[0]][3] or \
                self.components_dict[sku_list[0]][7] > self.components_dict[sku_list[4]][4]:
            # Compares:
            # Proc socket != MoBo socket
            # RAM type != MoBo ram type
            # MoBo RAM amount < user RAM amount
            # SSD type == m.2 and MoBo m.2 amount slots == 0
            # MoBo form-factor > case form-factor
            # GPU length > case gpu length
            # cooling socket != proc socket
            # proc tdp > cool tdp
            mb.showinfo('Information', message='The selected components are not compatible.')
        else:
            my_cursor.execute(f'''CALL insert_order_customer(\'{customer_number}\', {sku_list[0]}, {sku_list[4]}, 
                              {sku_list[3]}, {sku_list[9]}, {sku_list[1]}, {sku_list[2]}, {sku_list[7]}, {sku_list[6]}, 
                              {sku_list[5]}, {sku_list[8]}, \'commentaries\', \'in progress\');''')
            self.main_menu()
            self.place_output_window('New order was created!')


if __name__ == '__main__':
    god_engine = create_engine(god_url)
    god_cursor = god_engine.connect()
    update_is_exists()
    if is_exists == 0:
        connect_db()
    app = App()
    app.geometry(default_resolution + '+120+50')
    app.title("Database editor")
    app.resizable(width=False, height=False)
    app.main_menu()
    app.mainloop()
