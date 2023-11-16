import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    API_KEY = os.getenv('BOT_API_KEY')
    NEW_VACANCIES_CRON_TRIGGER = os.getenv('NEW_VACANCIES_CRON_TRIGGER', default='interval')
    NEW_VACANCIES_CRON_PERIOD = int(os.getenv('NEW_VACANCIES_CRON_PERIOD', default=60))

    SERVER_PARSE = os.getenv('SERVER_PARSE')
    SERVER_GPT = os.getenv('SERVER_GPT')

    POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE_TG')
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
