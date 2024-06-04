from tkinter import *
from dotenv import load_dotenv, set_key
from tkinter import ttk
import os
import os.path
import platform
import subprocess
env_file = '.env'
load_dotenv()

def aa():
    set_key(env_file, 'evlicense', '1')
    evtk_l.destroy()

def open_license():
    if os.path.exists("LICENSE.md"):
        system = platform.system()
        command = ""
        if system == "Windows":
            command = ['notepad.exe', 'LICENSE.md']

        elif system == "Darwin":
            command = ['open', 'LICENSE.md']

        elif system == 'Linux':
            command = ['xdg-open', 'LICENSE.md']

        subprocess.Popen(command)

if not os.getenv('evlicense') == '1':
    evtk_l = Tk()
    evtk_l.title("EV Launcher")
    evtk_l.iconbitmap(default="assets/ev-launcher_a.ico")
    evtk_l.geometry("300x400")

    label = ttk.Label(text="Согласитесь с лицензией")
    label.place(x=2.5, y=30)

    btn = Button(text="Не согласиться")
    btn.place(x=10, y=300)

    btn = Button(text="ОТКРЫТЬ ЛИЦЕНЗИЮ", command=open_license)
    btn.place(x=10, y=300)
    btn.configure(width=38, height=2)



    btn = Button(text="СОГЛАСИТЬСЯ", command=aa)
    btn.place(x=10, y=350)
    btn.configure(width=38, height=2)

    evtk_l.mainloop()

else:
    print("Вы согласны с лицензией")
