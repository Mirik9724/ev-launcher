import threading

def your_function(arg1, arg2):
 # ваш код здесь

# создание нового потока
thread = threading.Thread(target=your_function, args=(arg1, arg2))

# запуск потока
thread.start()
