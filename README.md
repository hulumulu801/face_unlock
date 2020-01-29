# face_unlock
Hello! These small scripts will allow you to unlock your PC in the face without entering a screenlock password.
Привет! Это небольшие скрипты позволят Вам разблокировать свой ПК по лицу не вводя пароля от screenlock.
Тестировались скрипты на Kali Linux(2019.2) и Ubuntu(18.04.3). На KAli Linux(2019.4) - РАБОТАТЬ НЕ БУДЕТ
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/0.png)
![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/0_1.png)

Скрипты запускаются автоматически(после первого входа в систему, т.е. первый ввод вводим username and password), благодоря supervisor.

01_face.py - Скрипт, который запоминает лицо по которому в дальнейшем будет происходить разблокировка screenlock.
02_face.py - Основной скрипт.

ВАЖНО, для запуска необходимо убедится, что бы путь до скриптов не имел русских букв.(Команда: pwd). Обращаем внимание на выделенное, см. рис. ниже.
