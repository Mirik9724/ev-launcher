from tkinter import *
from tkinter import ttk, filedialog
from dotenv import load_dotenv, set_key

import os
import platform
import sys


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

lblacces = Label(settk, text="Acess Token(Не меняйте если незнаете зачем)")
lblacces.place(relx=0.5, y=515, anchor='center')

lblnick = Label(settk, text="Nickname")
lblnick.place(relx=0.5, y=470, anchor='center')

lblramjvm= Label(settk, text="RAM для JVM в MB(Только целые числа)")
lblramjvm.place(relx=0.5, y=425, anchor='center')

spinboxramjvm_var = StringVar(value=os.getenv('ram_for_java'))

spinboxramjvm = ttk.Spinbox(from_=256, to=8192, increment=128, textvariable=spinboxramjvm_var)
spinboxramjvm.place(x=50, y=440)
spinboxramjvm.configure(width=54)

lblramjvm = ttk.Label(text="RAM: ")
lblramjvm.place(x=5, y=440)

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        entdir.delete(0, END)  # Очистка предыдущего значения в Entry
        entdir.insert(0, folder_path)  # Вставка нового пути


# Поле для отображения выбранного пути
entdir = Entry(width=22)
entdir.place(x=155, y=345)
entdir.insert(0, os.getenv('Directory'))

# Кнопка для вызова функции выбора папки
buttondir = Button(text="Выбрать папку", command=select_folder, width=13)
buttondir.place(x=295, y=345)

entWidth = Entry()
entWidth.place(x=160, y=375)
entWidth.configure(width=17)
entWidth.insert(0, os.getenv('custWidth'))

lbl1 = Label(text="X")
lbl1.place(x=270, y=375)

entHeight = Entry()
entHeight.place(x=290, y=375)
entHeight.configure(width=17)
entHeight.insert(0, os.getenv('custHeight'))

enabled = IntVar()
if os.getenv('evlicense') == "1":
    enabled.set(1)
else:
    enabled.set(0)

enabled2 = IntVar()
if os.getenv('custRel') == "1":
    enabled2.set(1)
else:
    enabled2.set(0)

enabled3 = IntVar()
if os.getenv('custDirectory') == "1":
    enabled3.set(1)
else:
    enabled3.set(0)

checkbuttondir = ttk.Checkbutton(text="Кастомная директория", variable=enabled3)
checkbuttondir.place(x=5, y=345)

checkbuttonrel = ttk.Checkbutton(text="Кастомное разрешение", variable=enabled2)
checkbuttonrel.place(x=5, y=375)

checkbuttonlic = ttk.Checkbutton(text="Согласие с лицензией", variable=enabled)
checkbuttonlic.place(x=5, y=395)

lblinfo = Label(settk, text=str(platform.node()) + "-" + platform.system() + " " + platform.release() + "-" + platform.machine())
lblinfo.place(x=5, y=5)

def save_settings():
    set_key(env_file, 'ram_for_java', str(spinboxramjvm.get()))
    set_key(env_file, 'accestoken', entyaccestoken.get())
    set_key(env_file, 'nickname', entynick.get())
    set_key(env_file, 'evlicense', str(enabled.get()))
    set_key(env_file, 'custRel',  str(enabled2.get()))
    set_key(env_file, 'custHeight', str(entHeight.get()))
    set_key(env_file, 'custWidth', str(entWidth.get()))
    set_key(env_file, 'custDirectory', str(enabled3.get()))
    set_key(env_file, 'Directory', str(folder_path))

    if os.getenv('evlicense') == '0':
        print("Вы отказались от лицензии")
        sys.exit()

btn = Button(text="СОХРАНИТЬ", command=save_settings, activebackground="#0a8b2e", background="green")
btn.place(x=5, y=555)
btn.configure(width=54, height=2)

settk.mainloop()