import os.path
import platform
import subprocess

if os.path.exists("logs/latest.log"):
    system = platform.system()
    command = ""
    if system == "Windows":
        command = ['notepad.exe', 'logs/latest.log']

    elif system == "Darwin":
        command = ['open', 'logs/latest.log']

    elif system == 'Linux':
        command = ['xdg-open', 'logs/latest.log']

    subprocess.Popen(command)