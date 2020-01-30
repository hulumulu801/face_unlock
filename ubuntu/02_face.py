#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import dlib
from skimage import io
from scipy.spatial import distance
from skimage.draw import polygon_perimeter
import glob
import os
import cv2
import sys
from PIL import Image
import uuid
import pickle
import re
import random
import shutil
from time import sleep
from keyboard import add_hotkey
from keyboard import wait

def unlock_screen():
    base_folder = "./"
    path = os.path.abspath(base_folder)
    abs_path = path + "/"
# Проверяем есть ли папки "Description_dataset" и "dataset"
    if os.path.exists(abs_path + "Description_dataset"):
        shutil.rmtree(abs_path + "Description_dataset", ignore_errors = True)
    if os.path.exists(abs_path + "dataset"):
        shutil.rmtree(abs_path + "dataset", ignore_errors = True)
# Подключаемся к камере
    cam = cv2.VideoCapture("/dev/video0") # Если путь отличается, МЕНЯЕМ ТУТ!!!!
    cam.set(3, 640) # установить ширину видео
    cam.set(4, 480) # установить высоту видео
    face_detector = cv2.CascadeClassifier(abs_path + 'haarcascade_frontalface_default.xml') # путь до Cascade, мы используем каскад Хаара по обнаружению лиц

    face_id = str(uuid.uuid4())
# Инициализация индивидуальной выборочной грани
    count = 0
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (20, 20)
        )

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
# Сохраните захваченное изображение в папку наборов данных
# Создадим папку
            folder = "./dataset"
            if not os.path.exists(folder):
                os.makedirs(folder)
            cv2.imwrite(folder + "/" + str(face_id) + '_' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        k = cv2.waitKey(100) & 0xff # Нажмите «ESC» для выхода из видео
        if k == 27:
            break
        elif count >= 3: # Взять 3 образцов лица и остановить видео
            break

    cam.release()
    cv2.destroyAllWindows()

# Извлекаем дескрипторы лица
    faces_folder_path = abs_path + "dataset" # Аргумент. Где ищем файлы .jpg(папка)
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(abs_path + 'shape_predictor_68_face_landmarks.dat')
    facerec = dlib.face_recognition_model_v1(abs_path + 'dlib_face_recognition_resnet_model_v1.dat')
    for f in glob.glob(os.path.join(faces_folder_path + "*/", "*.jpg")):
        img = dlib.load_rgb_image(f)
        dets = detector(img, 2)
# Теперь обработаем каждое лицо, которое мы нашли
        for k, d in enumerate(dets):
            polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()],
                                [d.right(), d.left(), d.left(), d.right()])
# находим уникальные точки на лице изображения
            shape = sp(img, d)
            face_descriptor = facerec.compute_face_descriptor(img, shape) # Вытаскиваем дескрипторы лица и сохроняем их в переменную face_descriptor
# Сохраняем выделенные дескрипторы в разные файлы .pickle
            filename = str(uuid.uuid4()) # даем нашему файлу .pickle уникальное имя с помощью библиотеке uuid
# Создаем папку Description и в нее сохроняем файлы .pickle
            newpath = abs_path + "Description_dataset"
            if not os.path.exists(newpath): # Проверяем есть ли она в директории
                os.makedirs(newpath) # Создаем папку
# Вытаскиваем из лица дескрипторы и сохроняем их в файл .pickle папку Description
            with open(abs_path + "Description_dataset/" + filename + '.pickle', 'wb') as file_save:
                pickle.dump(face_descriptor, file_save) # pickle.dump - сохранение дескрипторов в двоичный файл .pickle

    find_file = os.listdir(abs_path + "Description_database/") # Где ищем файлы
    find_file_1 = random.choice(find_file) # Выбираем рандомно один файл
    face_rec_model_path = os.path.abspath(abs_path + "Description_database/" + find_file_1) # узнаем абсолютный путь
    find_file_2 = os.listdir(abs_path + "Description_dataset/")
    find_file_3 = random.choice(find_file_2)
    faces_folder_path = os.path.abspath(abs_path + "Description_dataset/" + find_file_3)
# Сравниваем дискрипторы
    with open(face_rec_model_path, 'rb') as file_load:
        file_data_description_0 = pickle.load(file_load) # pickle.load - загружаем из двоичного файла .pickle наш дискриптор
    with open(faces_folder_path, 'rb') as file_load_1: # Открываем на чтение все, что находится в переменной f и задаем все в новую переменную file_load_1
        file_data_description_1 = pickle.load(file_load_1) # pickle.load - загружаем из всех файлов с расширением .pickle наши дискриптор
    a = distance.euclidean(file_data_description_0, file_data_description_1) # Рассчитываем Евклидово расстояние между двумя дексрипторами лиц
    f_1 = round(a, 2) # Округляем Евклидово расстояние между двумя дексрипторами лиц до двух знаков после запятой
    if 0 <= f_1 <= 0.45: # Если Евклидово расстояние между двумя дексрипторами лиц меньше или равно 0.45, то...
        os.system("sudo loginctl unlock-sessions") # Разблокируем экран блокировки
# Удаляем дискрипторы и фото лица
        shutil.rmtree(abs_path + "Description_dataset", ignore_errors = True)
        shutil.rmtree(abs_path + "dataset", ignore_errors = True)
    elif 0.46 <= f_1 <= 1: # Если Евклидово расстояние между двумя дексрипторами лиц больше 0.60, но меньше 1, выводим сообщение о не совпадении
        shutil.rmtree(abs_path + "Description_dataset", ignore_errors = True)
        shutil.rmtree(abs_path + "dataset", ignore_errors = True)

add_hotkey("Ctrl + 1", unlock_screen)
wait("Ctrl + 3")
