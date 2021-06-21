# 0. Exporting Geckodriver in a automated way
import os
import platform

## Add 'export geckodriver' line at the end of .bashrc only if this OS is Linux
if platform.system() == "Linux":
    path_to_geckodriver = os.path.abspath('geckodriver-v0.29.1-linux64')
    path_to_geckodriver = '"' + path_to_geckodriver + '"'

    file_to_read = open(os.path.join(os.getenv('HOME'), '.bashrc'), 'r')
    list_of_lines = file_to_read.readlines()
    file_to_read.close()

    if "geckodriver" not in list_of_lines[-1]:
        file = open(os.path.join(os.getenv('HOME'), '.bashrc'), 'a')
        file.write(f"\nexport PATH=$PATH:{path_to_geckodriver}")
        file.close()