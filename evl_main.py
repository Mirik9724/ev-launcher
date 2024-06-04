from tkinter import *
from tkinter import ttk
import minecraft_launcher_lib
import subprocess
from dotenv import load_dotenv, set_key

from random_username.generate import generate_username
from uuid import uuid1
import os
import threading
from PIL import ImageTk

evlversion = "0.7"
env_file = '.env'
load_dotenv()
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def printPRbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()
    progressbar.step(1)

def maximum(max_value, value):
    max_value[0] = value

max_value = [0]

callback = {
    "setStatus": lambda text: print(text),
    "setProgress": lambda value: printProgressBar(value, max_value[0]),
    "setMax": lambda value: maximum(max_value, value)
}



ram_for_java =  os.getenv('ram_for_java')
fabric_loader_version = minecraft_launcher_lib.fabric.get_latest_loader_version()

def settings_w():
    subprocess.call(['python', 'evl_settings.py'])

evtk = Tk()
evtk.title("EV Launcher v" + evlversion)
evtk.iconbitmap(default="assets/ev-launcher_a.ico")
evtk.geometry("300x400")

usernameumol = ""

if os.getenv('nickname') in ('', None):
    usernameumol = ""
else:
    usernameumol = os.getenv('nickname')

entusername = Entry()
entusername.insert(0, usernameumol)
entusername.place(x=10, y=275)
entusername.configure(width=46)

# lbl = Label(text="Выберите версию")
# lbl.place(x=40, y=320)

versions = ["1.19.4", "1.20.1", "1.20.4"]
versions_var = StringVar(value=versions[0])

vcombobox = ttk.Combobox(textvariable=versions_var, values=versions)
vcombobox.place(x=10, y=300)
vcombobox.configure(width=43, height=2)
# vcombobox.set(1)

versionc = str(vcombobox.get())  #versions_var.get()
minecraft_directoryc = ".ev-game" #minecraft_launcher_lib.utils.get_minecraft_directory().replace('.minecarft', '.ev-launcher')

prvalue_var = IntVar(value=0)

progressbar = ttk.Progressbar(orient="horizontal", variable=prvalue_var, length=280, maximum=1)
progressbar.place(x=10, y=325)


label = ttk.Label(textvariable=str(prvalue_var) + "%")
label.place(x=270, y=325)

def launch_game():
    # minecraft_launcher_lib.runtime.install_jvm_runtime("17.0.8", minecraft_directoryc, None)
    # if minecraft_launcher_lib.fabric.FabricMinecraftVersion:

    minecraft_launcher_lib.fabric.install_fabric(str(versions_var.get()), minecraft_directory=minecraft_directoryc, callback=callback)
    print("Файлы успешно установлены")

    username = entusername.get()
    set_key(env_file, 'nickname', username)
    if entusername.get() == "":
        username = "Player"

    options = {
        'username': str(username),
        'uuid': str(uuid1()),
        'token': '',
        "server": "95.216.30.27",
        "port": "25801",
        "jvm Arguments": ["-Xincgc", "-Xmx" + ram_for_java + "M", "-Xms256M"],
        "launcher Name": "EV-Launcher",
        "launcher Version": evlversion,
        "gameDirectory": minecraft_directoryc,
        "demo": False
    }

    print("Запуск Minecraft")
    subprocess.call(
        minecraft_launcher_lib.command.get_minecraft_command(version="fabric-loader-" + fabric_loader_version + "-" + str(versions_var.get()), minecraft_directory=minecraft_directoryc,
                                                             options=options))

def launch_thread():
    threadlau = threading.Thread(target=launch_game, args=())
    threadlau.start()

def open_lasted_log():
    subprocess.call(['python', 'evl_latest_log.py'])
    # file_lasted_lod = open('logs/latest.log', 'r')
    # # os.open("logs/latest.log", 'r')
    #
    # llogtk = Tk()
    # llogtk.title("Логи(последние)")
    # llogtk.geometry("300x700")
    #
    # btns = Button(llogtk, text="ВЫЙТИ", command=llogtk.destroy, activebackground="#cd0000", background="red")
    # btns.place(x=100, y=0)
    #
    # lbllog = Label(llogtk, text=file_lasted_lod)
    # lbllog.place(x=10, y=350)
    #
    # llogtk.mainloop()
    # file_lasted_lod.close()


btn = Button(text="СТАРТ", command=launch_thread, activebackground="#0a8b2e", background="green")
btn.place(x=10, y=350)
btn.configure(width=34, height=2)

img = PhotoImage(file="assets/mc_title_.png")

# img = Image.open("assets/mc_title.png")
# img = img.resize((290, 82))
# img = ImageTk.PhotoImage(img)

label = ttk.Label(evtk, image=img)
label.place(x=2.5, y=30)

btn = Button(text="ЛОГИ", command=open_lasted_log)
btn.place(x=250, y=350)
btn.configure(width=4, height=2)

btnnews = Button(text="НОВОСТИ МАЙНКРАФТА")
btnnews.place(x=0, y=0)
btnnews.configure(width=22, height=1)

btns = Button(text="НАСТРОЙКИ", command=settings_w, activebackground="#c8c8c8")
btns.place(x=165, y=0)

btns = Button(text="ВЫЙТИ", command=evtk.destroy, activebackground="#cd0000", background="red")
btns.place(x=250, y=0)

evtk.mainloop()


