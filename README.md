# skills-guide_telegram

Сервис проекта skills_guide по работе с ботом telegram 

![](https://img.shields.io/badge/aiogram-3.1.1-00CED1)
![](https://img.shields.io/badge/SQLAlchemy-2.0.22-DC143C)



## 🛠️ Подготовка в запуску

1. [Download and install Python](https://www.python.org/downloads/) (Version 3.10+ is recommended).

2. Клонируйте репозиторий GitHub:
```bash
git clone https://github.com/acronicsM/skills-guide_telegram.git
```
3. Перейдите в директорию проекта:
```bash
cd skills-guide_telegram
```
4. Установите переменные окружения:
```bash
nano .env
```
5. (Рекомендуется) Создайте виртуальную среду Python::
[Python official documentation](https://docs.python.org/3/tutorial/venv.html).


```
python3 -m venv venv
```

6. Активируйте виртуальную среду:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
7. Установите необходимые пакеты Python из `requirements.txt`:

```
pip install -r requirements.txt
```

8. Запустите `main.py`

## 🙌 Необходимы переменные окружения

1. BOT_API_KEY - Token бота
2. POSTGRES_PASSWORD - Пароль пользователя для подключения к postgre
3. POSTGRES_HOST - адрес хоста бд postgre 
4. POSTGRES_PORT - порт хоста бд postgre 
5. POSTGRES_DATABASE_TG - имя БД postgre 
6. SERVER_PARSE - адрес сервиса __skills-guide_parser__
7. SERVER_GPT - адрес сервиса __skills-guide_gpt__
8. NEW_VACANCIES_CRON_TRIGGER - Тип периодичности проверки новых вакансий для подписчиков ``date``, ``interval`` или ``cron``
9. NEW_VACANCIES_CRON_PERIOD - Периодичность проверки новых вакансий
