from tkinter import *
from dotenv import load_dotenv, set_key

import os
import platform


settk = Tk()
settk.title("Настройки")
settk.geometry("400x600")
settk.iconbitmap(default="assets/ev-launcher_a.ico")
env_file = '.env'
load_dotenv()

# val = IntVar(value=10)

# ramScale = ttk.Scale(settk, orient=HORIZONTAL, length=230, from_=256, to=8192, value=2048)
# ramScale.place(x=10, y=20)
# ram_for_java = ramScale.get()

entyaccestoken = Entry()
entyaccestoken.place(x=5, y=530)
entyaccestoken.configure(width=64)
# custum_path_to_java = ttk.Checkbutton(text="Костомный путь до Java")
# custum_path_to_java.pack(padx=6, pady=6, anchor=NW)

entynick = Entry()
entynick.place(x=5, y=485)
entynick.insert(0, os.getenv('nickname'))
entynick.configure(width=64)

lblacces = Label(settk, text="Acces Token(Не меняйте если незнаете зачем)")
lblacces.place(relx=0.5, y=515, anchor='center')

lblnick = Label(settk, text="Nickname")
lblnick.place(relx=0.5, y=470, anchor='center')

lblramjvm= Label(settk, text="RAM для JVM в MB(Только целые числа)")
lblramjvm.place(relx=0.5, y=425, anchor='center')

entramjvm = Entry()
entramjvm.place(x=5, y=440)
entramjvm.insert(0, os.getenv('ram_for_java'))
entramjvm.configure(width=64)

lblinfo = Label(settk, text=str(platform.node()) + " " + platform.system() + " " + platform.machine())
lblinfo.place(x = 5 ,y = 5)

def save_settings():
    set_key(env_file, 'ram_for_java', str(entramjvm.get()))
    set_key(env_file, 'accestoken', entyaccestoken.get())
    set_key(env_file, 'nickname', entynick.get())

btn = Button(text="СОХРАНИТЬ", command=save_settings, activebackground="#0a8b2e", background="green")
btn.place(x=5, y=555)
btn.configure(width=54, height=2)

settk.mainloop()



