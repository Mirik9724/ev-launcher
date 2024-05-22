import sys
import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(
 "%s" % (i.key) for i in installed_packages
)
libs = ['minecraft-launcher-lib', 'pillow', 'random-username']

if libs[0] in installed_packages_list and libs[1] in installed_packages_list and libs[2] in installed_packages_list:
 print("Все библиотеки устоновленны")
else:
  print("Устоновите библиотеки lbs_install_all_libs_for_windows.bat или обновите lbs_update_all_libs_for_windows.bat")
  sys.exit()