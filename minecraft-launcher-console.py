import sys
import minecraft_launcher_lib
import subprocess
from uuid import uuid1
from random_username.generate import generate_username
import threading

ru_l = ["Введите версию: ", "Введите ник: ", "(если его нету нечего не вводите): ", "Загрузчик модов('fabric', 'forge', 'нету'): ", "Сколько RAM выделить в Gygabyte: "]
en_l = ["Enter version: ", "Enter nickname: ", "(if you don't have one, don't enter anything): ", "Mod loader('fabric', 'forge', 'no'): ", "How much RAM to allocate in Gygabyte: "]
ru_l_s = ["Версия не найдена", "Fabric не поддерживает эту версию", "Forge не поддерживает эту версию"]
en_l_s = ["Version not found", "Fabric does not support this version", "Forge does not support this version"]
l_l = []
l_l_s = []

fabric_loader_new = minecraft_launcher_lib.fabric.FabricLoader

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    if iteration == total:
        print()

def maximum(max_value, value):
    max_value[0] = value


minecraft_directory = ".gudu" #minecraft_launcher_lib.utils.get_minecraft_directory()
lang = input("язык|language 'ru' or|или 'en': ")
if lang == "ru":
    l_l = ru_l
    l_l_s = ru_l_s
else:
    l_l = en_l
    l_l_s = en_l_s

versionc = input(l_l[0])
username = input(l_l[1])
uuidc = input("UUID" + l_l[2])
access_token = input("Access token" + str(l_l[2]) + ": ")
loader = input(l_l[3])
ram_for_java = input(l_l[4])
ffv = minecraft_launcher_lib.forge.find_forge_version(versionc)
print('=======================================================================================')

max_value = [0]
callback = {
        "setStatus": lambda text: print(text),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
}
def install_mc(versionc, loader):
    if loader == "forge":
        if minecraft_launcher_lib.forge.supports_automatic_install(versionc):
            print(l_l_s[2])
            sys.exit()

        else:
            pass
        minecraft_launcher_lib.forge.install_forge_version(minecraft_launcher_lib.forge.find_forge_version(versionc), minecraft_directory, callback=callback)
        # support = minecraft_launcher_lib.forge.support_automatic_install(versionc)


    if loader == "fabric":
        if minecraft_launcher_lib.fabric.is_minecraft_version_supported(versionc):
            pass

        else:
            print(l_l_s[1])
            sys.exit()

        minecraft_launcher_lib.fabric.install_fabric(str(versionc), minecraft_directory, callback=callback)


    else:
      # if True:
        #     minecraft_launcher_lib.install.List()
        #
        # else:
       #     print(l_l_s[0])
       #     sys.exit()

        minecraft_launcher_lib.install.install_minecraft_version(versionid=versionc,
                                                             minecraft_directory=minecraft_directory, callback=callback)

# threadinstall_mc = threading.Thread(target=install_mc, args=(versionc, loader))
# threadinstall_mc.start()
install_mc(versionc, loader)

def launch_mc(uuidc, username):
    if username == "" or " ":
        username = generate_username()[0]
    if uuidc == "" or " ":
        uuidc = uuid1()

    options = {
        'username': str(username),
       'uuid': str(uuidc),
       'token': str(access_token)
    }
    options["jvmArguments"] = ["-Xmx" + ram_for_java + "G", "-Xms128m"]
    options["gameDirectory"] = minecraft_directory

    if loader == "fabric":
        pass
        # subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(
        #     version="fabric-loader-" + str(fabric_loader_new) + "-" + str(versionc), minecraft_directory=minecraft_directory,
        #     options=options))

    if loader == "forge":
        subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(
            version=str(versionc) + "-forge-" + ffv.replace(versionc + "-", ""), minecraft_directory=minecraft_directory,
            options=options))

    else:
      subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(
            version=str(versionc), minecraft_directory=minecraft_directory,
            options=options))

threadlaunch_mc = threading.Thread(target=launch_mc, args=(uuidc, username))
# threadlaunch_mc.start()
launch_mc(uuidc, username)

#-Xincgc