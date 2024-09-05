from tkinter import *
import os
import zipfile
import platform
import requests
import threading
import subprocess
from tkinter import filedialog, messagebox
import sys

url = "https://github.com/Mirik9724/ev-launcher/archive/refs/heads/main.zip"

evlinstaller = Tk()
evlinstaller.title("EV Launcher installer")
evlinstaller.geometry("300x400")


def download_file(url, dest):
    response = requests.get(url)
    with open(dest, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {dest}")


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted to {extract_to}")


def install_dependencies(path):
    subprocess.run(["python", "-m", "venv", "env"], cwd=path)
    activate_script = os.path.join(path, "env", "Scripts" if platform.system() == "Windows" else "bin", "activate")

    if platform.system() == "Windows":
        subprocess.run([activate_script], shell=True)
    else:
        subprocess.run(["source", activate_script], shell=True)

    subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=path)


def start_installation():
    dest_folder = folder_entry.get()

    if not dest_folder:
        messagebox.showerror("Ошибка", "Пожалуйста, укажите папку для распаковки")
        return

    ev_launcher_folder = os.path.join(dest_folder, ".ev-launcher")
    os.makedirs(ev_launcher_folder, exist_ok=True)

    zip_path = os.path.join(ev_launcher_folder, "main.zip")

    try:
        download_file(url, zip_path)
        extract_zip(zip_path, ev_launcher_folder)

        project_folder = os.path.join(ev_launcher_folder, "ev-launcher-main")
        install_dependencies(project_folder)

        messagebox.showinfo("Успех", "Установка завершена успешно")
        folder_entry.delete(0, END)
        folder_entry.insert(0, os.path.join(dest_folder, ".ev-launcher"))
        output_label.config(text=f"Установлено в: {ev_launcher_folder}/ev-launcher")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, END)
        folder_entry.insert(0, folder_selected)


lbl = Label(text="Папка для програмы с добавлением  .ev-launcher").place(x=5, y=100)
folder_entry = Entry(width=40)
folder_entry.place(x=5, y=70)
browse_button = Button(text="Обзор", command=browse_folder).place(x=250, y=70)

lblinfo = Label(text=str(platform.node()) + " " + platform.system() + " " + platform.machine())
lblinfo.place(x=5, y=5)


def install():
    start_installation()


def install_thread():
    threadinstall = threading.Thread(target=install, args=())
    threadinstall.start()


btn = Button(text="Установить", command=install_thread, activebackground="#0a8b2e", background="green")
btn.place(x=5, y=310)
btn.configure(width=40, height=2)

btns = Button(text="Выйти", command=evlinstaller.destroy, activebackground="#cd0000", background="red")
btns.place(x=5, y=355)
btns.configure(width=40, height=2)

output_label = Label(evlinstaller, text="")
output_label.place(x=5, y=270)

evlinstaller.mainloop()
