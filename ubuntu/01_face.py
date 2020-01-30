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
import shutil
base_folder = "./"
path = os.path.abspath(base_folder)
abs_path = path + "/"
# Подключаемся к камере
cam = cv2.VideoCapture("/dev/video0") # Если путь отличается, МЕНЯЕМ ТУТ!!!!
cam.set(3, 640) # установить ширину видео
cam.set(4, 480) # установить высоту видео
face_detector = cv2.CascadeClassifier(abs_path + 'haarcascade_frontalface_default.xml') # путь до Cascade, мы используем каскад Хаара по обнаружению лиц
# Присваиваем имя
face_id = str(uuid.uuid4())
print("\n [INFO] Инициализация захвата лица. Смотрите в камеру и ждите ...")
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
        folder = "./database"
        if not os.path.exists(folder):
            os.makedirs(folder)
        cv2.imwrite(folder + "/" + str(face_id) + '_' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    k = cv2.waitKey(100) & 0xff # Нажмите «ESC» для выхода из видео
    if k == 27:
        break
    elif count >= 30: # Взять 30 образцов лица и остановить видео
        break
cam.release()
cv2.destroyAllWindows()
# Извлекаем дескрипторы лица
faces_folder_path = "./database" # Аргумент. Где ищем файлы .jpg(папка)
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
win = dlib.image_window()
for f in glob.glob(os.path.join(faces_folder_path + "*/", "*.jpg")):
    img = dlib.load_rgb_image(f)
    win.clear_overlay()
    win.set_image(img)
    dets = detector(img, 2)
    print("Найдено лиц: {}".format(len(dets)))
# Теперь обработаем каждое лицо, которое мы нашли
    for k, d in enumerate(dets):
        polygon_perimeter([d.top(), d.top(), d.bottom(), d.bottom()],
                            [d.right(), d.left(), d.left(), d.right()])
# находим уникальные точки на лице изображения
        shape = sp(img, d) # находим уникальные точки на лице изображения
# Нарисуем ориентиры лица на экране, чтобы мы могли видеть, какое лицо в настоящее время обрабатывается.
        win.clear_overlay()
        win.add_overlay(d)
        win.add_overlay(shape)
        face_descriptor = facerec.compute_face_descriptor(img, shape) # Вытаскиваем дескрипторы лица и сохроняем их в переменную face_descriptor
# Сохраняем выделенные дескрипторы в разные файлы .pickle
        filename = str(uuid.uuid4()) # даем нашему файлу .pickle уникальное имя с помощью библиотеке uuid
# Создаем папку Description и в нее сохроняем файлы .pickle
        newpath = "./Description_database"
        if not os.path.exists(newpath): # Проверяем есть ли она в директории
            os.makedirs(newpath) # Создаем папку
# Вытаскиваем из лица дескрипторы и сохроняем их в файл .pickle папку Description
        with open("./Description_database/" + filename + '.pickle', 'wb') as file_save:
            pickle.dump(face_descriptor, file_save) # pickle.dump - сохранение дескрипторов в двоичный файл .pickle
# Удаляем папку с фотками лиц
shutil.rmtree(faces_folder_path, ignore_errors = True)
