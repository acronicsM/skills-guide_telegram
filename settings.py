import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    API_KEY = os.getenv('BOT_API_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    NEW_VACANCIES_CRON_TRIGGER = os.getenv('NEW_VACANCIES_CRON_TRIGGER', default='interval')
    NEW_VACANCIES_CRON_PERIOD = int(os.getenv('NEW_VACANCIES_CRON_PERIOD', default=60))

    SERVER_PARSE = 'http://127.0.0.1:5000'
    SERVER_GPT = 'http://127.0.0.1:7000'
