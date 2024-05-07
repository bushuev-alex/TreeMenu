
  <h3 align="center">Сервис генерации древовидного меню</h3>

### Условие задания:
* Меню реализовано через template tag;
* Все, что над выделенным пунктом - развернуто.
Первый уровень вложенности под выделенным пунктом тоже развернут;
* Хранится в БД;
* Редактируется в стандартной админке Django;
* Активный пункт меню определяется исходя из URL текущей страницы;
* Меню на одной странице может быть несколько, они определяются по названию;
* При клике на меню происходит переход по заданному в нем URL.
Он может быть задан как явным образом, так и через named URL;
* На отрисовку каждого меню требуется ровно 1 запрос к БД.

Нужен django-app, который позволяет вносить в БД меню (одно или несколько)через админку,
и нарисовать на любой нужной странице меню по названию.{% draw_menu 'main_menu' %}
При выполнении задания из библиотек следует использовать только Django истандартную библиотеку Python.

### Используемый стек технологий в проекте:
* Django
* django-tree-queries
* PostgreSQL

### Перед запуском выполните:
* Склонировать репозиторий в локальную директорию:\
  ```git clone git@github.com:bushuev-alex/TreeMenu.git```\
  или через https\
  ```git clone https://github.com/bushuev-alex/TreeMenu.git```


* Активация виртуального окружения и создание зависимостей:\
  ```python3.11 -m venv venv```\
  ```pip install -r requirements.txt```


* В корне Django-проекта (первая папка ```treemenu```) создайте ```.env``` и задайте значения переменных:\
  ```DJANGO_SECRET_KEY```=\
  ```DB_NAME```=\
  ```DB_USER```=\
  ```DB_PASSWORD```=\
  ```DB_HOST```=\
  ```DB_PORT```=


* Создайте базу данных ```DB_NAME``` и дайте привилегии для пользователя ```DB_USER```:\
  ```sudo -i -u postgres```\
  ```psql```\
  ```CREATE DATABASE``` ```DB_NAME```;\
  ```GRANT ALL PRIVILEGES ON DATABASE``` ```DB_NAME``` to ```DB_USER```;\
  ```GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO``` ```DB_USER```;\
  ```GRANT ALL ON SCHEMA public TO postgres```;


* Cоздание администратора и миграций, а также их применение:\
  ```python manage.py makemigrations```\
  ```python manage.py migrate```\
  ```python manage.py createsuperuser```
