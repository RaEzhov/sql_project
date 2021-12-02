import tkinter as tk
import tkinter.messagebox as mb

default_width = 1280
default_height = 720
default_font = 'Terminal'
default_resolution = f'{default_width}x{default_height}'


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #background image
        self.filename = tk.PhotoImage(file='./bg_im.gif')
        self.background_label = tk.Label(self, image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.button_background = tk.Canvas(self, width=400, height=720, bg="#90c", highlightthickness=0)

        self.b1 = tk.Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b2 = tk.Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b3 = tk.Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b4 = tk.Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b5 = tk.Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b6 = tk.Button(text='Button', width=12,  height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
        self.b7 = tk.Button(text='Button', width=12,  height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)

        self.b1.place(x=930, y=20)
        self.b2.place(x=930, y=120)
        self.b3.place(x=930, y=220)
        self.b4.place(x=930, y=320)
        self.b5.place(x=930, y=420)
        self.b6.place(x=930, y=520)
        self.b7.place(x=1110, y=520)

        self.info_output = tk.Label(width=83, height=20, font=default_font+' 20', text='helloooooo\nthis is text', foreground='#222', background='#93c', borderwidth=5,  relief="ridge", anchor='nw')
        self.info_output.place(x=20, y=100)

        self.button_background.create_line(5, 5, 395, 5, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(395, 5, 395, 715, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 395, 715, fill='#528', dash=(40, 40), width=5)
        self.button_background.create_line(5, 715, 5, 5, fill='#528', dash=(40, 40), width=5)
        self.button_background.pack(side=tk.RIGHT)

    def hello(self):
        msg = 'Hello, world!'
        mb.showerror('Info', msg)


if __name__ == '__main__':
    app = App()
    app.geometry(default_resolution + '+120+50')
    app.title("Database editor")
    app.resizable(width=False, height=False)
    app.mainloop()
