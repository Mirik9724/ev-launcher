import time

with open('logs/latest.log', 'r') as file:
    content = file.read()
    print("Последние логи:\n")
    time.sleep(0.5)
    print(content)