import tkinter as tk
from tkinter import ttk


def callbackFunc():
    print("New Element Selected")


app = tk.Tk()
app.geometry('200x100')


def changeMonth():
    comboExample["values"] = ["July",
                              "August",
                              "September",
                              "October"
                              ]



labelTop = tk.Text(width=154, height=20)
labelTop.insert(tk.INSERT, 'Hell0')
labelTop.configure(state='disabled')
labelTop.place(x=0, y=0)

comboExample = ttk.Combobox(app,
                           values=[
                               "January",
                               "February",
                               "March",
                               "April"],
                           postcommand=callbackFunc)

comboExample.place(x=10, y=10)

app.mainloop()
