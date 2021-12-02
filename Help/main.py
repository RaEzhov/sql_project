from tkinter import *
import tkinter.messagebox as mb

root = Tk()

# input = '{Width}x{Height}{}{}'
root.geometry('800x600-600-200')
root.title("My GUI Experiments")

# Label
l1 = Label(text="Утренние пары по БД", font='Arial 32')
l2 = Label(text="AWERSOME", font='Arial 18')
l3 = Label(text="Database", font='Arial 18')
l4 = Label(text="Thanks GOD of War", font='Arial 18')
# 1
l1['bg'] = '#ffaaaa'
# 2
l1.config(bd=40)
l3['bg'] = '#000000'
l3['fg'] = '#FFFFFF'

# l1.place(anchor=CENTER, relx=0.5, rely=0.9)
# l2.place(anchor=SE, x=450, y=281)
# l3.place(anchor=CENTER, relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
# l4.place(anchor=NW, relx=0.1, rely=0.3)
#



# Button

def changer(btn, entry):
    def change():
        answer = mb.askyesno(title="Уверены?", message="Вы уверены что хотите поменят кнопку?")
        if answer == True:
            btn['text'] = 'Изменено'
            btn['bg'] = '#000000'
            btn['fg'] = '#ffffff'
            btn['activebackground'] = '#555555'
            btn['activeforeground'] = '#Aadd55'
            print(f"DEBUG:: entry = {entry.get()}")
            mb.showinfo(title="Info", message="Кнопка изменена")
    return change


b1 = Button(text='Push me!', width=15, height=5)



# Entry
e1 = Entry(width=50)
e1.insert(0, 'Example entry insertion')
e1.insert(8, 'Example entry insertion')
e1.pack()

b1.config(command=changer(b1, e1))

b1.pack()

# Radiobutton Checkbox
var = IntVar()
var.set(2)
r1 = Radiobutton(text='Radio 1', variable=var, value=1)
r2 = Radiobutton(text='Radio 2', variable=var, value=2)
print(f"DEBUG:: var = {var.get()}")
ch1 = Checkbutton(text='Checkbutton 1', variable=var, onvalue=1, offvalue=2)

r1.pack()
r2.pack()
ch1.pack()

# listbox
lst = Listbox(selectmode=EXTENDED)
for i in range(20):
    lst.insert(END, f"generated {i}")

def addItem():
    lst.insert(END, e1.get())

def delItems():
    select = list(lst.curselection())
    select = reversed(select)
    for i in select:
        lst.delete(i)

def log():
    print("DEBUG:: listbox = \n\t {}".format('\n\t'.join(lst.get(0, END))))

add = Button(text='Add item', command=addItem)
delete = Button(text='DElete item', command=delItems)
loging = Button(text='Log to console listbox ', command=log)

lst.pack()
add.pack()
delete.pack()
loging.pack()




root.mainloop()
