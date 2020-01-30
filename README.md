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

- открываем терминал и вставляем следующее содержимое:

    cd --
    
    git clone https://github.com/hulumulu801/face_unlock.git
    
 # Если UBUNTU:
 
 - mv face_unlock/ubuntu/ /home/ТУТ_ПИШЕМ_ИМЯ_ПОЛЬЗОВАТЕЛЯ/

- rm -rf face_unlock/

- cd ubuntu/

- Запускаем инсталятор(install.py). Он установит dlib и supervisor.

    sudo python3 install.py
    
 - Проверяем как запустился supervisor. Если все ок, то должно быть как на рис. ниже. Обращаем внимание на выделенное, см. рис. ниже.

    service supervisor status
    
    ![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/2.png)
    
- Запускаем первый скрипт и смотрим в камеру:

 python3 01_face.py
 
- Проверяем, блокируем экран командой(сочетание клавишь):

    SUPER + L
    
- Разблокируем экран(сочетание клавишь):

    CTRL + 1

Горячую клавишу("CTRL + 1") можно изменять на любые, смотри 02_face.py строка 116

Строка 117 - выход из скрипта, т.е. чтобы занова запустить скрипт 02_face.py в демоне нужно перезагрузить supervisor(sudo service supervisor restart)

# Если Kali Linux:

- mv face_unlock/kali_linux/ /root/

- rm -rf face_unlock/

- cd kali_linux/

- Запускаем инсталятор(install.py). Он установит dlib и supervisor.

    python3 install.py

- Проверяем как запустился supervisor. Если все ок, то должно быть как на рис. ниже. Обращаем внимание на выделенное, см. рис. ниже.

    service supervisor status
    
    ![Image alt](https://github.com/hulumulu801/face_unlock/blob/master/pict/2_2.png)
    
 - Запускаем первый скрипт и смотрим в камеру:
    
    python3 01_face.py
    
- Проверяем, блокируем экран командой(сочетание клавишь):

    SUPER + L
    
- Разблокируем экран(сочетание клавишь):

    Ctrl + A + 4

Сочетание клавиш ("Ctrl + A + 4") можно изменять на любые, смотри 02_face.py строка 116. Да и вообще, можно сделать генератор горячих клавиш, при каждом заблокированном экране нам на почту будет отсылаться комбинация клавиш.

Строка 117 - выход из скрипта, т.е. чтобы занова запустить скрипт 02_face.py в демоне нужно перезагрузить supervisor(service supervisor restart)

P.S. Это примитивное распознование лица, т.е. по картинки то же распознает, не стоит на него расчитывать) но очень удобно, когда у Вас пароль очень длинный и вводить надоедает
