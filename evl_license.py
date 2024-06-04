from tkinter import *
from dotenv import load_dotenv, set_key
from tkinter import ttk
import os
env_file = '.env'
load_dotenv()

def aa():
    set_key(env_file, 'nickname', 'Player_gudu')
    evtk_l.destroy()

if os.getenv('evlicense') == 0:
    print("Вы отказались от лицензии")
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

else:
    print("Вы согласны с лицензией")
