from tkinter import Button, Canvas, PhotoImage, Label, Tk, Text, Entry, Checkbutton, ttk
import tkinter
import tkinter.messagebox as mb

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

default_pg_login = 'user'
default_pg_passwd = 'password'
default_pg_host = 'localhost'
default_pg_port = '5432'
default_pg_db_name = 'pc_shop'
pg_url = f'postgresql://' \
         f'{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/{default_pg_db_name}'
god_url = f'postgresql://{default_pg_login}:{default_pg_passwd}@{default_pg_host}:{default_pg_port}/god'
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
table_names_dict = {'Processor': 0, 'Motherboard': 1, 'Graphics card': 2, 'RAM': 3, 'Cooling': 4, 'Power supply': 5,
                    'SSD': 6, 'HDD': 7, 'Case': 8}
other_tables = ['order_customer', 'customer']

names_of_columns = [['Brand', 'Model', 'Socket', 'Cores', 'Threads', 'Integrated GPU', 'TDP'],
                    ['Brand', 'Model', 'Socket', 'Chipset', 'RAM type', 'RAM slots', 'Form-factor', 'M.2 slots'],
                    ['Chip',  'Brand', 'Model', 'Memory capacity', 'Memory type', 'Length'],
                    ['Brand', 'Model', 'Type', 'Capacity', 'Frequency', 'Modules'],
                    ['Brand', 'Model', 'Socket', 'TDP'],
                    ['Brand', 'Model', 'Power'],
                    ['Brand', 'Model', 'Capacity', 'Form factor'],
                    ['Brand', 'Model', 'Capacity', 'Rotation speed', 'Form factor'],
                    ['Brand', 'Model', 'Form factor', 'GPU length']]


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


def sku_is_right(sku, table_num):
    if int(sku[0]) != table_num + 1:
        mb.showinfo('Information', message='Wrong SKU!')
        return False
    return True


def add_spaces(lst):
    if len(lst) == 0:
        lst = ['']
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


def num_in_list(number, list_numbers):
    for i in list_numbers:
        if str(number) in str(i):
            return True
    return False


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
        self.insert_text_list = []
        self.insert_entries_list = []
        self.input_changer = 0

        self.option_add("*TCombobox*Listbox.Font", default_font)

        self.button_background = Canvas(self, width=1280, height=270,
                                        bg=default_button_bg_color, highlightthickness=0)
        self.sku_entry = Entry(font=default_font, background=additional_color_1, foreground=default_info_win_color,
                               width=4)
        self.sku_text = Text(font=default_font, width=4, height=1, bg=default_info_win_color,
                             fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.sku_text.insert(tkinter.INSERT, 'SKU:')
        self.sku_text.configure(state='disabled')

        self.sku_amount_entry = Entry(font=default_font, background=additional_color_1,
                                      foreground=default_info_win_color, width=4)
        self.sku_amount_text = Text(font=default_font, width=7, height=1, bg=default_info_win_color,
                                    fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.sku_amount_text.insert(tkinter.INSERT, 'Amount:')
        self.sku_amount_text.configure(state='disabled')

        self.customer_comment_entry = Entry(font=default_font, background=additional_color_1,
                                            foreground=default_info_win_color, width=30)
        self.customer_phone_entry = Entry(font=default_font, background=additional_color_1,
                                          foreground=default_info_win_color, width=11)
        self.customer_comment_text = Text(font=default_font, width=17, height=1, bg=default_info_win_color,
                                          fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.customer_comment_text.insert(tkinter.INSERT, 'Customer comment:')
        self.customer_comment_text.configure(state='disabled')

        self.customer_first_name_entry = Entry(font=default_font, background=additional_color_1,
                                               foreground=default_info_win_color, width=11)
        self.customer_last_name_entry = Entry(font=default_font, background=additional_color_1,
                                              foreground=default_info_win_color, width=11)
        self.customer_first_name_entry.insert(tkinter.INSERT, 'First name')
        self.customer_last_name_entry.insert(tkinter.INSERT, 'Last name')

        self.order_id_entry = Entry(font=default_font, background=additional_color_1,
                                    foreground=default_info_win_color, width=10)
        self.order_id_text = Text(font=default_font, width=17, height=1, bg=default_info_win_color,
                                  fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.order_id_text.insert(tkinter.INSERT, 'Order ID:')
        self.order_id_text.configure(state='disabled')

        self.is_new_customer = tkinter.IntVar()
        self.new_customer_checkbox = Checkbutton(text='New customer', font=default_font,
                                                 background=default_button_bg_color,
                                                 variable=self.is_new_customer,
                                                 activebackground=default_button_bg_color,
                                                 onvalue=1, offvalue=0, command=self.update_first_last_name_entry)
        self.customer_phone_text = Text(font=default_font, width=15, height=1, bg=default_info_win_color,
                                        fg=default_info_font_color, wrap=tkinter.WORD, bd=0)
        self.customer_phone_text.insert(tkinter.INSERT, 'Customer phone:')
        self.customer_phone_text.configure(state='disabled')
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
        self.complete_cancel_button = Button(text='Complete/cancel order', command=self.complete_cancel_order_menu,
                                             image=self.button_image, compound='center',
                                             foreground=default_font_color,
                                             border=0,
                                             background=default_button_bg_color,
                                             activebackground=default_button_bg_color,
                                             activeforeground=default_active_font_color, font=default_button_font)
        self.update_db_menu_button = Button(text='Update Database', command=self.update_db_menu,
                                            image=self.button_image, compound='center',
                                            foreground=default_font_color,
                                            border=0,
                                            background=default_button_bg_color,
                                            activebackground=default_button_bg_color,
                                            activeforeground=default_active_font_color, font=default_button_font)
        self.update_db_button = Button(text='Update amount of this SKU', command=self.update_db,
                                       image=self.button_image, compound='center',
                                       foreground=default_font_color,
                                       border=0,
                                       background=default_button_bg_color,
                                       activebackground=default_button_bg_color,
                                       activeforeground=default_active_font_color, font=default_button_font)
        self.complete_order_button = Button(text='Complete', command=self.complete_order,
                                            image=self.button_image, compound='center',
                                            foreground=default_font_color, border=0,
                                            background=default_button_bg_color,
                                            activebackground=default_button_bg_color,
                                            activeforeground=default_active_font_color,
                                            font=default_button_font)
        self.cancel_order_button = Button(text='Cancel', command=self.cancel_order,
                                          image=self.button_image, compound='center',
                                          foreground=default_font_color, border=0,
                                          background=default_button_bg_color,
                                          activebackground=default_button_bg_color,
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
        self.add_product_button = Button(text='Add product', command=self.add_product,
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
                                        foreground=default_font_color,
                                        image=self.button_half_image, compound='center', border=0,
                                        background=default_button_bg_color, activebackground=default_button_bg_color,
                                        activeforeground=default_active_font_color, font=default_button_font)
        self.sku_delete_button = Button(text='SKU delete', command=self.sku_delete,
                                        foreground=default_font_color,
                                        image=self.button_half_image, compound='center', border=0,
                                        background=default_button_bg_color, activebackground=default_button_bg_color,
                                        activeforeground=default_active_font_color, font=default_button_font)

    def select_proc(self):
        data = my_cursor.execute(f'''SELECT * FROM return_proc();''')
        output = []
        columns = ['SKU'] + names_of_columns[0] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[1] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[2] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[3] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[4] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[5] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[6] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[7] + ['Price', 'Amount']
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
        columns = ['SKU'] + names_of_columns[8] + ['Price', 'Amount']
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
        self.insert_entries_list = []
        update_is_exists()
        self.update_connection_status()
        if is_exists == 1:
            self.new_order_button['state'] = 'disabled'
            self.show_db_menu_button['state'] = 'disabled'
            self.clearing_tables_button['state'] = 'disabled'
            self.complete_cancel_button['state'] = 'disabled'
            self.update_db_menu_button['state'] = 'disabled'
        else:
            self.new_order_button['state'] = 'normal'
            self.show_db_menu_button['state'] = 'normal'
            self.clearing_tables_button['state'] = 'normal'
            self.complete_cancel_button['state'] = 'normal'
            self.update_db_menu_button['state'] = 'normal'
        self.show_db_menu_button.place(x=20, y=520)
        self.buttons_list.append(self.show_db_menu_button)
        self.new_order_button.place(x=20, y=620)
        self.buttons_list.append(self.new_order_button)
        self.actions_with_db_button.place(x=340, y=520)
        self.buttons_list.append(self.actions_with_db_button)
        self.complete_cancel_button.place(x=660, y=520)
        self.buttons_list.append(self.complete_cancel_button)
        self.update_db_menu_button.place(x=660, y=620)
        self.buttons_list.append(self.update_db_menu_button)
        self.clearing_tables_button.place(x=340, y=620)
        self.buttons_list.append(self.clearing_tables_button)
        self.exit_button.place(x=1120, y=620)
        self.buttons_list.append(self.exit_button)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.place_output_window('')
        self.button_background.place(x=0, y=450)

    def complete_order(self):
        session = Session(my_engine)
        order_id = self.order_id_entry.get()
        if order_id == '':
            mb.showinfo('Information', message='Order ID is empty!')
            return
        if order_id.isdigit():
            is_available = list(session.execute(f'SELECT is_available_order({int(order_id)})'))[0][0]
            if is_available == 1:
                session.execute(f'''CALL change_status_complete_order({int(order_id)});''')
                self.place_output_window('Order was completed!')
            else:
                mb.showinfo('Information', message='Order with this ID does not exists or it\'s status not \'in '
                                                   'progress\'')
        else:
            mb.showinfo('Information', message='Wrong Order ID!')
        session.commit()
        session.close()

    def cancel_order(self):
        session = Session(my_engine)
        order_id = self.order_id_entry.get()
        if order_id == '':
            mb.showinfo('Information', message='Order ID is empty!')
            return
        if order_id.isdigit():
            sku_list = list(session.execute(f'SELECT return_sku_with_order_id({order_id});'))
            if not sku_list:
                mb.showinfo('Information', message='Order with this ID does not exists!')
                return
            sku_list = list(map(int, sku_list[0][0][1:-1].split(',')))
            is_available = list(session.execute(f'SELECT is_available_order({int(order_id)})'))[0][0]
            if is_available == 1:
                session.execute(f'''CALL change_status_cancel_order({int(order_id)}, {sku_list[0]}, {sku_list[1]}, 
                                {sku_list[2]}, {sku_list[3]}, {sku_list[4]}, {sku_list[5]}, {sku_list[6]}, 
                                {sku_list[7]}, {sku_list[8]}, {sku_list[9]});''')
                self.place_output_window('Order was canceled!')
            else:
                mb.showinfo('Information', message='Order with this ID does not exists or it\'s status not \'in '
                                                   'progress\'')
        else:
            mb.showinfo('Information', message='Wrong Order ID!')
        session.commit()
        session.close()

    def complete_cancel_order_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)
        self.show_order_button.place(x=340, y=620)
        self.buttons_list.append(self.show_order_button)

        self.order_id_text.place(x=330, y=535)
        self.buttons_list.append(self.order_id_text)

        self.order_id_entry.place(x=330, y=560)
        self.buttons_list.append(self.order_id_entry)
        self.order_id_entry.delete(0, tkinter.END)
        self.order_id_entry.insert(0, "")

        self.complete_order_button.place(x=20, y=520)
        self.buttons_list.append(self.complete_order_button)
        self.cancel_order_button.place(x=20, y=620)
        self.buttons_list.append(self.cancel_order_button)

    def clear_tables_menu(self):
        self.place_output_window('')
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
        session = Session(my_engine)
        for i in range(9):
            table = self.checkbox_values[i].get()
            if table == 1:
                query = f'CALL clear_{names_of_tables[i]}();'
                session.execute(query)
        self.main_menu()
        self.place_output_window('Chosen tables was cleared!')
        session.commit()
        session.close()

    def clear_all_tables(self):
        session = Session(my_engine)
        query = f'''CALL clear_all_tables();'''
        session.execute(query)
        session.commit()
        session.close()
        self.main_menu()
        self.place_output_window('All tables was cleared.')

    def add_product(self):
        session = Session(my_engine)
        if self.input_changer.get() == '':
            mb.showinfo('Information', message='Table not chosen.')
            return
        args_list = []
        table_num = table_names_dict[self.input_changer.get()]
        args_amount = len(names_of_columns[table_num])
        for entry in self.insert_entries_list:
            args_list.append(entry.get())
        for i in range(len(args_list)):
            if (i < args_amount + 1 or i > len(args_list) - 3) and args_list[i] == '' and (table_num != 3 or i != 2):
                mb.showinfo('Information', message='One or more fields are empty!')
                return
        if not args_list[0].isdigit() or len(args_list[0]) != 4:
            mb.showinfo('Information', message='SKU is not supported!')
            return
        if not sku_is_right(args_list[0], table_num):
            return
        if table_num == 0:  # processor
            session.execute(f'CALL insert_proc({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'\'{args_list[3]}\', {args_list[4]}, {args_list[5]}, \'{args_list[6]}\', {args_list[7]}, '
                            f'{args_list[-2]}, {args_list[-1]})')
        elif table_num == 1:  # motherboard
            session.execute(f'CALL insert_motherboard({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'\'{args_list[3]}\', \'{args_list[4]}\', \'{args_list[5]}\', {args_list[6]}, \''
                            f'{args_list[7]}\', {args_list[8]}, {args_list[-2]}, {args_list[-1]})')
        elif table_num == 2:  # graphics card
            session.execute(f'CALL insert_gpu({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'\'{args_list[3]}\', {args_list[4]}, \'{args_list[5]}\', {args_list[6]}, {args_list[-2]}, '
                            f'{args_list[-1]})')
        elif table_num == 3:  # ram
            session.execute(f'CALL insert_ram({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'\'{args_list[3]}\', {args_list[4]}, {args_list[5]}, {args_list[6]}, {args_list[-2]}, '
                            f'{args_list[-1]})')
        elif table_num == 4:  # cooling
            session.execute(f'CALL insert_cool({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', \''
                            f'{args_list[3]}\', {args_list[4]}, {args_list[-2]}, {args_list[-1]})')
        elif table_num == 5:  # power supply
            session.execute(f'CALL insert_power_supply({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'{args_list[3]}, {args_list[-2]}, {args_list[-1]})')
        elif table_num == 6:  # ssd
            session.execute(f'CALL insert_ssd({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', {args_list[3]}, '
                            f'\'{args_list[4]}\', {args_list[-2]}, {args_list[-1]})')
        elif table_num == 7:  # hdd
            session.execute(f'CALL insert_hdd({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', {args_list[3]}, '
                            f'{args_list[4]}, \'{args_list[5]}\', {args_list[-2]}, {args_list[-1]})')
        elif table_num == 8:  # case
            session.execute(f'CALL insert_case_pc({args_list[0]}, \'{args_list[1]}\', \'{args_list[2]}\', '
                            f'\'{args_list[3]}\', {args_list[4]}, {args_list[-2]}, {args_list[-1]})')
        self.place_output_window('New product was added.')
        session.commit()
        session.close()

    def input_entries_place(self, event):
        for txt in self.insert_text_list:
            txt.place_forget()
        self.insert_text_list = []
        for entry in self.insert_entries_list:
            entry.place_forget()
        self.insert_entries_list = []
        insert_y = 388
        insert_y_upper = 55
        table = self.input_changer.get()
        table_num = table_names_dict[table]
        self.insert_text_list = ['SKU:', 'Price:', 'Amount:'] + names_of_columns[table_num]
        insert_text_list_len = len(self.insert_text_list)
        for ind in range(insert_text_list_len):
            self.insert_text_list[ind] = Label(text=self.insert_text_list[ind], font=default_font,
                                               background=default_info_win_color,
                                               foreground=default_info_font_color, bd=0)
        self.insert_text_list[0].place(x=30, y=insert_y - insert_y_upper)
        self.insert_text_list[1].place(x=120, y=insert_y - insert_y_upper)
        self.insert_text_list[2].place(x=250, y=insert_y - insert_y_upper)
        for i in range(3, insert_text_list_len):
            self.insert_text_list[i].place(x=150 * (i - 3) + 30, y=insert_y - 25)
        self.insert_entries_list.append(Entry(font=default_font, background=additional_color_1,
                                              foreground=default_info_win_color, width=4))
        self.insert_entries_list[0].place(x=70, y=insert_y - insert_y_upper)
        for i in range(1, 9):
            self.insert_entries_list.append(Entry(font=default_font, background=additional_color_1,
                                                  foreground=default_info_win_color, width=16,
                                                  disabledbackground=default_info_win_color))
            if i <= len(self.insert_text_list) - 3:
                self.insert_entries_list[i].place(x=150 * i - 122, y=insert_y)
        self.insert_entries_list.append(Entry(font=default_font, background=additional_color_1,
                                              foreground=default_info_win_color, width=6))
        self.insert_entries_list[9].place(x=180, y=insert_y - insert_y_upper)

        self.insert_entries_list.append(Entry(font=default_font, background=additional_color_1,
                                              foreground=default_info_win_color, width=2))
        self.insert_entries_list[10].place(x=320, y=insert_y - insert_y_upper)
        for i in range(10):
            self.buttons_list.append(self.insert_entries_list[i])

    def update_db_menu(self):
        for button in self.buttons_list:
            button.place_forget()
        self.buttons_list = []
        self.go_to_main_menu_button.place(x=1120, y=620)
        self.buttons_list.append(self.go_to_main_menu_button)
        self.update_db_button.place(x=20, y=620)
        self.buttons_list.append(self.update_db_button)
        self.sku_entry.place(x=100, y=520)
        self.buttons_list.append(self.sku_entry)
        self.sku_text.place(x=30, y=520)
        self.buttons_list.append(self.sku_text)
        self.sku_amount_entry.place(x=100, y=560)
        self.buttons_list.append(self.sku_amount_entry)
        self.sku_amount_text.place(x=30, y=560)
        self.buttons_list.append(self.sku_amount_text)
        self.sku_entry.delete(0, tkinter.END)
        self.sku_entry.insert(0, "")
        self.sku_amount_entry.delete(0, tkinter.END)
        self.sku_amount_entry.insert(0, "")
        self.input_changer = ttk.Combobox(self, font=default_font, width=15, state='readonly', values=['Processor',
                                                                                                       'Motherboard',
                                                                                                       'Graphics card',
                                                                                                       'RAM',
                                                                                                       'Cooling',
                                                                                                       'Power supply',
                                                                                                       'SSD',
                                                                                                       'HDD',
                                                                                                       'Case'],
                                          background=default_info_win_color)
        self.input_changer.bind('<<ComboboxSelected>>', self.input_entries_place)
        self.input_changer.place(x=500, y=520)
        self.buttons_list.append(self.input_changer)
        self.add_product_button.place(x=340, y=620)
        self.buttons_list.append(self.add_product_button)
        chose_table = Label(text='Choose table to add:', font=default_font,
                            background=default_info_win_color,
                            foreground=default_info_font_color, bd=0)
        chose_table.place(x=312, y=522)
        self.buttons_list.append(chose_table)

    def update_db(self):
        amount = self.sku_amount_entry.get()
        if not amount.isdigit():
            mb.showinfo('Information', message='Amount is not number!')
        else:
            amount = int(amount)
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
                    session = Session(my_engine)
                    session.execute(f'CALL update_amount_{names_of_tables[int(sku[0]) - 1]}({sku}, {amount});')
                    self.place_output_window(res_str + f'<- old amount\n{amount} - new amount.')
                    session.commit()
                    session.close()
                else:
                    mb.showinfo('Information', message='SKU not found!')

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

    def update_first_last_name_entry(self):
        if self.is_new_customer.get() == 0:
            self.customer_first_name_entry.configure(state='disabled')
            self.customer_last_name_entry.configure(state='disabled')
        else:
            self.customer_first_name_entry.configure(state='normal')
            self.customer_last_name_entry.configure(state='normal')

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

        self.customer_phone_text.place(x=1008, y=481)
        self.buttons_list.append(self.customer_phone_text)

        self.customer_phone_entry.place(x=1150, y=480)
        self.buttons_list.append(self.customer_phone_entry)
        self.customer_phone_entry.delete(0, tkinter.END)
        self.customer_phone_entry.insert(0, "")

        self.customer_comment_text.place(x=820, y=531)
        self.buttons_list.append(self.customer_comment_text)

        self.customer_comment_entry.place(x=980, y=530)
        self.buttons_list.append(self.customer_comment_entry)
        self.customer_comment_entry.delete(0, tkinter.END)
        self.customer_comment_entry.insert(0, "")

        self.customer_first_name_entry.place(x=820, y=580)
        self.buttons_list.append(self.customer_first_name_entry)
        self.customer_first_name_entry.delete(0, tkinter.END)
        self.customer_first_name_entry.insert(0, "")
        self.customer_first_name_entry.insert(0, "First name")

        self.customer_last_name_entry.place(x=1000, y=580)
        self.buttons_list.append(self.customer_last_name_entry)
        self.customer_last_name_entry.delete(0, tkinter.END)
        self.customer_last_name_entry.insert(0, "")
        self.customer_last_name_entry.insert(0, "Last name")

        self.is_new_customer.set(0)
        self.new_customer_checkbox.place(x=820, y=480)
        self.buttons_list.append(self.new_customer_checkbox)

        self.update_first_last_name_entry()

        self.combo_boxes = []
        self.components_dict = {}
        for i in range(9):
            data = my_cursor.execute(f'''SELECT * FROM return_{names_of_tables[i]}();''')
            output = []

            for j in data:
                if j[-1] > 0:
                    output.append(list(j))
                    self.components_dict[j[0]] = j
            output_choose = []
            add_spaces(output)
            for k in output:
                output_str = ''
                for j in k:
                    output_str += j
                output_choose.append(output_str)
            make_list_of_str(output)
            self.combo_boxes.append(ttk.Combobox(self, font=default_font, values=output_choose, width=106,
                                                 state='readonly'))
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

    def sku_delete(self):
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
                query = f'CALL delete_with_sku_{names_of_tables[int(sku[0]) - 1]}({sku});'
                my_cursor.execute(query)
                self.place_output_window(f'Position with sku = {sku} was deleted!\n{res_str}')
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

        self.sku_delete_button.place(x=1120, y=520)
        self.buttons_list.append(self.sku_delete_button)

        self.sku_entry.place(x=1190, y=495)
        self.buttons_list.append(self.sku_entry)
        self.sku_entry.delete(0, tkinter.END)
        self.sku_entry.insert(0, "")

        self.sku_text.place(x=1150, y=497)
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
        customers_list = list(my_cursor.execute('SELECT * FROM return_customer();'))
        for i in range(10):
            sku_list.append(self.combo_boxes[i].get()[0:4])
        customer_number = self.customer_phone_entry.get()
        if len(customer_number) != 11 or not customer_number.isdigit():
            mb.showinfo('Information', message='Customer phone number is not supported!')
        elif '' in sku_list or '0' in sku_list[9]:
            mb.showinfo('Information', message='Not all components selected!')
        elif self.components_dict[int(sku_list[0])][3] != self.components_dict[int(sku_list[1])][3] or \
                self.components_dict[int(sku_list[3])][3] != self.components_dict[int(sku_list[1])][5] or \
                self.components_dict[int(sku_list[1])][6] < int(sku_list[9]) * \
                self.components_dict[int(sku_list[3])][6] or \
                self.components_dict[int(sku_list[6])][4] == 'm.2' and \
                self.components_dict[int(sku_list[1])][8] == '0' or \
                motherboard_form_factor_dict[self.components_dict[int(sku_list[1])][7]] > \
                motherboard_form_factor_dict[self.components_dict[int(sku_list[8])][3]] or \
                self.components_dict[int(sku_list[2])][6] > self.components_dict[int(sku_list[8])][4] or \
                self.components_dict[int(sku_list[0])][3] != self.components_dict[int(sku_list[0])][3] or \
                self.components_dict[int(sku_list[0])][7] > self.components_dict[int(sku_list[4])][4]:
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
        elif self.is_new_customer.get() == 0 and not num_in_list(customer_number, customers_list):
            mb.showinfo('Information', message='There is no such phone number in '
                                               'the list of customers. Add new customer!')
        elif int(sku_list[9]) > self.components_dict[int(sku_list[3])][8]:
            mb.showinfo('Information', message='There is no such amount of RAM in stock!')
        else:
            session = Session(my_engine)
            if self.is_new_customer.get() == 1:
                session.execute(f'''CALL insert_customer(\'{customer_number}\', 
                                \'{self.customer_first_name_entry.get()}\', 
                                \'{self.customer_last_name_entry.get()}\');''')
            session.execute(f'''CALL insert_order_customer(\'{customer_number}\', {sku_list[0]}, {sku_list[4]}, 
                              {sku_list[3]}, {sku_list[9]}, {sku_list[1]}, {sku_list[2]}, {sku_list[7]}, {sku_list[6]}, 
                              {sku_list[5]}, {sku_list[8]}, \'{self.customer_comment_entry.get()}\', 
                              \'in progress\');''')
            session.commit()
            session.close()
            self.main_menu()
            self.place_output_window('New order was created!')


if __name__ == '__main__':
    god_engine = create_engine(god_url)
    god_cursor = god_engine.connect()
    update_is_exists()
    if is_exists == 0:
        connect_db()
    app = App()
    app.geometry(default_resolution + '+120+30')
    app.title("Database editor")
    app.resizable(width=False, height=False)
    app.main_menu()
    app.mainloop()
