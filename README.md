# face_unlock
Hello! These small scripts will allow you to unlock your PC in the face without entering a screenlock password.

Привет! Это небольшие скрипты позволят Вам разблокировать свой ПК по лицу не вводя пароля от screenlock.

Тестировались скрипты на Kali Linux(2019.2) и Ubuntu(18.04.3). На Kali Linux(2019.4) - РАБОТАТЬ НЕ БУДЕТ

Теперь не нужно вводить логин и пароль от screenlock.
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/0.png)
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/0_1.png)
Скрипты запускаются автоматичеси благодоря supervisor.

01_face.py - Скрипт, который запоминает лицо по которому в дальнейшем будет происходить разблокировка screenlock.

02_face.py - Основной скрипт.

ВАЖНО, для запуска необходимо убедится, что бы путь до скриптов не имел русских букв.(Команда: pwd). Обращаем внимание на выделенное, см. рис. ниже.
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/1.png)

Ваша камера должна иметь путь /dev/video0, если отличается путь, исправляем в 01_face.py и 02_face.py

Проверяем, подключена ли камера(Команда: ls /dev/):
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/0_2.png)

# Как установить?

git clone https://github.com/hulumulu801/face_unlock.git

