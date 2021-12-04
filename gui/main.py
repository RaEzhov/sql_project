from tkinter import Button, Canvas, PhotoImage, Label, Tk
import tkinter
import tkinter.messagebox as mb
from sqlalchemy import create_engine
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
default_font_color = '#639'             # 639
default_active_font_color = '#639'      # 639
default_button_color = '#cf0'           # cf0
default_active_button_color = '#9c0'    # 9c0
default_button_bg_color = '#90c'        # 90c
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

        # background image
        self.filename = PhotoImage(file='./bg_im.gif')
        self.background_label = Label(self, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_background = Canvas(self, width=400, height=720,
                                        bg=default_button_bg_color, highlightthickness=0)

        self.b1 = Button(text='Create DB', command=self.create_my_database, width=30, height=3, font=default_font+' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b2 = Button(text='Drop DB', command=self.drop_my_database, width=30, height=3, font=default_font+' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b3 = Button(text='Button3', command=hello, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b4 = Button(text='Button4', command=hello, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b5 = Button(text='Button5', command=hello, width=30, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b6 = Button(text='Button6', command=hello, width=12, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)
        self.b7 = Button(text='Button7', command=hello, width=12, height=3, font=default_font + ' 20',
                         background=default_button_color, foreground=default_font_color,
                         activebackground=default_active_button_color, activeforeground=default_active_font_color, bd=5)

        self.b1.place(x=930, y=20)
        self.b2.place(x=930, y=120)
        self.b3.place(x=930, y=220)
        self.b4.place(x=930, y=320)
        self.b5.place(x=930, y=420)
        self.b6.place(x=930, y=520)
        self.b7.place(x=1110, y=520)

        self.info_output = Label(width=83, height=20, font=default_font+' 20', text=f'{output_text}', foreground='#222',
                                 background='#93c', borderwidth=5,  relief="ridge", anchor='nw')
        self.info_output.place(x=20, y=100)

        self.button_background.create_line(5, 5, 395, 5, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(395, 5, 395, 715, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 395, 715, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 5, 5, fill='#528', dash=(40, 40), width=5)
        self.button_background.pack(side=tkinter.RIGHT)

    def place_output_window(self, info):
        self.info_output = Label(width=83, height=20, font=default_font + ' 20', text=f'{info}', foreground='#222',
                                 background='#93c', borderwidth=5, relief="ridge", anchor='nw')
        self.info_output.place(x=20, y=100)

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

