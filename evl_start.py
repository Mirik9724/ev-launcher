from dotenv import load_dotenv
import subprocess
import os
import sys

load_dotenv()
evlicese = os.getenv('evlicense')
if int(evlicese) == 1:
    pass
else:
    print("Вы отказались от лицензии")
    sys.exit()
subprocess.call(['python', 'evl_check_libs.py'])
# subprocess.call(['python', 'evl_license.py'])
subprocess.call(['python', 'evl_main.py'])
