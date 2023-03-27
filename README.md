# О проекте

RESTful API для управления заметками позволяет пользователям создавать, изменять и удалять свои заметки. API также поддерживает поиск по заметкам (реализовано с помощью библиотек soundex и thefuzz). Пользовательские запросы реализованы через токены.

## Используемые технологии
* Django
* DRF
* PostgreSQL
* Nginx
* Docker и Docker Compose

## Установка

1. Клонируйте репозиторий:

```bash
git clone git@github.com:N1ghtmarus/your_own_browser.git
```

2. Перейдите в каталог проекта и установите все необходимые зависимости:

```bash
cd backend
pip install -r requirements.txt
```
3. Создайте файл .env в корне проекта со следующим содержимым (замените значения на свои):
```makefile
DJANGO_SECRET_KEY=<>
DATABASE_POSTGRE_NAME=<>
DATABASE_POSTGRE_USER=<>
DATABASE_POSTGRE_PASSWORD=<>
DATABASE_POSTGRE_HOST=<>
DATABASE_POSTGRE_PORT=<>
```
4.  Выполните миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```
5. Запустите сервер разработки Django:

```bash
python manage.py runserver
```
Сервер будет доступен по адресу http://127.0.0.1:8000/.

## Запуск с использованием Docker

1. Убедитесь, что у вас установлен Docker и Docker Compose.

2. В каталоге проекта выполните следующую команду:

```bash
docker-compose up
```

Сервер будет доступен по адресу http://localhost/.

## Эндпоинты

Все URL для эндпоинтов начинаются с http://localhost:80/api/ или http://127.0.0.1:8000/api/ в зависимости от способа запуска.

### Получение токена
Для работы с API, необходимо получить токен авторизации. Это можно сделать, отправив POST-запрос на `/auth/token/login/` с полями username и password, содержащими имя пользователя и пароль. В ответ на запрос будет возвращен токен, который необходимо передавать в заголовке Authorization для всех последующих запросов:

* `/api/users/` - для получения списка пользователей
* `/api/users/<id>` - для получения информации о пользователе с заданным идентификатором
* `/api/note_admin/` - для выполнения CRUD-операций с заметками только для администратора
* `/api/create_note/` - для создания заметки
* `/api/search_note/<query>/` - для поиска заметок по ключевым словам
* `/api/update_note/<id>/` - для обновления существующей заметки
* `/api/delete_note/<id>/` - для удаления существующей заметки
* `/api/get_users_notes/` - для получения списка заметок, созданных пользователем

## Автор
* Arkhip Petin