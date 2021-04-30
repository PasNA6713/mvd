# Setup backend
1. Необходим рабочий Postgres (localhost:5432)
2. Для работы вебсокетов и парсинга необходимы Redis (localhost:6379), Celery (работает только под Linux)
3. Данные для подключения Postgres необходимо указать в файле .env (см example.env)
4. Необходимо создать окружение для работы проекта `python -m venv venv`. Рекомендуемы версия языка 3.7+
   Активация окружения `source <env_name>/bin/activate` - Linux, `cd <env_name>/Scripts` - `activate.bat` - Windows
5. Затем необходимо произвести установку необходимых библиотек в окружение `pip install -r requirements.txt`
6. `celery -A config worker -l info` - активация воркера Celery, должен работать параллельно с приложением
7. Необходимо произвести инициализирующие миграции в БД `python manage.py makemigretions` and `python manage.py migrate`
8. `python manage.py runserver` - произведет запуск asgi сервера daphne, доступного по `http://127.0.0.1:8000/`
9. `http://127.0.0.1:8000/swagger/` - документация проекта

P.S. В отсутствии пакетов nltk, необходимо произвести их установку
 
# Setup frontend
1. Необходимы NodeJS 12+, npm 6+, VueJS 2
2. Произвести `npm install` в директории frontend для установки необходимых пакетов
3. `npm run serve` - запуск проекта