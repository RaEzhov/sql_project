from tkinter import *

default_width = 1280
default_height = 720
default_font = 'Terminal'
default_resolution = f'{default_width}x{default_height}'


root = Tk()
root.geometry(default_resolution+'+120+50')
root.title("Database editor")
root.resizable(width=False, height=False)



#background image
filename = PhotoImage(file='./bg_im.gif')
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


button_background = Canvas(root, width=400, height=720, bg="#90c", highlightthickness=0)
button_background.pack(side=RIGHT)


b1 = Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b2 = Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b3 = Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b4 = Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b5 = Button(text='Button', width=30, height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b6 = Button(text='Button', width=12,  height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b7 = Button(text='Button', width=12,  height=3, font=default_font+' 20', background='#cf0', foreground='#639', activebackground='#9c0', activeforeground='#639', bd=5)
b1.place(x=930, y=20)
b2.place(x=930, y=120)
b3.place(x=930, y=220)
b4.place(x=930, y=320)
b5.place(x=930, y=420)
b6.place(x=930, y=520)
b7.place(x=1110, y=520)

info_output = Label(width=83, height=20, font=default_font+' 20', text='helloooooo\nthis is text', foreground='#222', background='#93c', borderwidth=5,  relief="ridge", anchor='nw')
info_output.place(x=20, y=100)


root.mainloop()
