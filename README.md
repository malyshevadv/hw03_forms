# Бекенд для социальной сети блогеров (backend_community_homework, часть yatube_project)

[![CI](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw03_forms/actions/workflows/python-app.yml)

### Описание
Бекенд для социальной сети блогеров.

Создано и подключено приложение core. 

Создано и подключено приложение about (страницы /about/author/, /about/tech/).

Подключено приложение django.contrib.auth.

Создано и подключено приложение users, переопределены шаблоны для авторизации (/auth/login/) и выхода изу аккаунта (/auth/logout/). Создана страница /auth/signup/ с формой для регистрации пользователей.

В приложении posts: 
  Создана страница пользователя profile/<username>/. На ней отображаются посты пользователя.
  
  Создана отдельная страница поста posts/<post_id>/.
  
  Подключен паджинатор.
  
  Создана навигация по разделам — это было в уроке «Добавляем навигацию в шаблоны».

### Технологии
Python 3.7
Django 2.2.19
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
### Авторы
Дарья М.
