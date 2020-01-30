#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import system
from os import path
from time import sleep

path = path.abspath("./")
abs_path_dlib = path + "/"
abs_path_pip = path + "/" + "reqarement.txt"

# Скачиваем shape_predictor_68_face_landmarks.dat
system("wget http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 && bunzip2 shape_predictor_68_face_landmarks.dat.bz2")

# Устанавливаем dlib
system("apt-get update && apt-get install build-essential cmake -y && apt-get install libopenblas-dev liblapack-dev -y")
system("apt-get install libx11-dev libgtk-3-dev -y && apt-get install python python-dev python-pip -y && apt-get install python3 python3-dev python3-pip -y && apt-get install cmake -y")
system("wget https://files.pythonhosted.org/packages/05/57/e8a8caa3c89a27f80bc78da39c423e2553f482a3705adc619176a3a24b36/dlib-19.17.0.tar.gz")
system("tar -xvzf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")
system("python3 " + str(abs_path_dlib) + "dlib-19.17.0/" + "setup.py install")
system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0/")
system("rm -rf " + str(abs_path_dlib) + "dlib-19.17.0.tar.gz")

# Устанавливаем pip'ы
system("pip3 install -r" + str(abs_path_pip))

# Устанавливаем supervisor
system("apt-get install supervisor")
# Редактируем файлы supervisor'a
system("touch /etc/supervisor/conf.d/screen_unlock.conf")
sleep(2)
data_1 = [
"""[program:screen_unlock]
command=python3 02_face.py
directory=""" + str(path)
]
data_2 = [
"""
stdout_logfile=""" + str(path) + "/" + """face_unlock.log
autostart=true
autorestart=true
redirect_stderr=true
"""
]
data = data_1 + data_2

with open("/etc/supervisor/conf.d/screen_unlock.conf", "w") as f:
    for d in data:
        f.write(str(d))
system("systemctl enable supervisor.service")
system("service supervisor restart")
