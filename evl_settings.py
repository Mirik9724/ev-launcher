from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv, set_key

settk = Tk()
settk.title("Настройки")
settk.geometry("250x200")
env_file = '.env'
load_dotenv()

val = IntVar(value=10)

ramScale = ttk.Scale(settk, orient=HORIZONTAL, length=230, from_=256, to=8192, value=2048)
ramScale.place(x=10, y=20)
ram_for_java = ramScale.get()

def save_settings():
    set_key(env_file, 'ram_for_java', str(ram_for_java))
    

btn = Button(text="СОХРАНИТЬ", command=save_settings, activebackground="#0a8b2e", background="green")
btn.place(x=10, y=350)
btn.configure(width=34, height=2)

lblset = Label(settk, textvariable=val)
lblset.place(x=70, y=100)

settk.mainloop()