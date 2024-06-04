from dotenv import set_key, load_dotenv
import os

env_file = '.env'
load_dotenv()

if not os.path.exists(env_file):
    with open(env_file, 'w') as file:
        pass
    set_key(env_file, 'evlicense', '0')
    set_key(env_file, 'nickname', '')
    set_key(env_file, 'ram_for_java', '2')
    set_key(env_file, 'versionmc', '')