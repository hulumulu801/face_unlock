#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system
from os import path
from time import sleep

path = path.abspath("./")
abs_path_dlib = path + "/"
abs_path_pip = path + "/" + "reqarement.txt"

# Скачиваем shape_predictor_68_face_landmarks.dat
system("sudo wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && sudo bunzip2 shape_predictor_68_face_landmarks.dat.bz2")

# Устанавливаем dlib
system("sudo apt-get update && sudo apt-get install build-essential cmake -y && sudo apt-get install libopenblas-dev liblapack-dev -y")
system("sudo apt-get install libx11-dev libgtk-3-dev -y && sudo apt-get install python python-dev python-pip -y && sudo apt-get install python3 python3-dev python3-pip -y && sudo apt-get install cmake -y")
system("sudo apt-get install python-matplotlib python-numpy python-pil python-scipy -y")
system("wget https://files.pythonhosted.org/packages/05/57/e8a8caa3c89a27f80bc78da39c423e2553f482a3705adc619176a3a24b36/dlib-19.17.0.tar.gz")
system("tar -xvzf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")
system("python3 " + str(abs_path_dlib) + "dlib-19.17.0/" + "setup.py install")
system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0/")
system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")

# Устанавливаем pip'ы
system("sudo -H pip3 install -r" + str(abs_path_pip))

# Устанавливаем supervisor
system("sudo apt-get install supervisor -y")
# Редактируем файлы supervisor'a
system("sudo touch /etc/supervisor/conf.d/screen_unlock.conf")
sleep(2)
d_1 = [
"[program:screen_unlock]"
]
d_2 = [
"\ncommand=sudo python3 02_face.py "
]
d_3 = [
"\ndirectory=" + str(path)
]
d_4 = [
"\nstdout_logfile=" + str(path) + "/" + "face_unlock.log"
]
d_5 = [
"\nautostart=true"
]
d_6 = [
"\nautorestart=true"
]
d_7 = [
"\nredirect_stderr=true"
]

data = d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7

with open("/etc/supervisor/conf.d/screen_unlock.conf", "w") as f:
    for d in data:
        f.write(str(d))
system("sudo systemctl enable supervisor.service")
system("sudo service supervisor restart")
