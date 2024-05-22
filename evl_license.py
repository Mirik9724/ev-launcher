from tkinter import *
from tkinter import ttk
import pickle
a = 0
data = {"agree_license": a}
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    data = pickle.load(f)

def aa():
    a = 1

if data == {"argee_license": 1}:
    evtk_l = Tk()
    evtk_l.title("EV Launcher")
    evtk_l.iconbitmap(default="assets/ev-launcher_a.ico")
    evtk_l.geometry("300x400")

    label = ttk.Label(text="Согласитесь с лицензией")
    label.place(x=2.5, y=30)

    btn = Button(text="ОТКРЫТЬ ЛИЦЕНЗИЮ")
    btn.place(x=10, y=300)
    btn.configure(width=38, height=2)



    btn = Button(text="СОГЛАСИТЬСЯ", command=aa)
    btn.place(x=10, y=350)
    btn.configure(width=38, height=2)

    evtk_l.mainloop()