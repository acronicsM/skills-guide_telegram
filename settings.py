import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    API_KEY = os.getenv('BOT_API_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')

    SERVER_PARSE = 'http://127.0.0.1:5000'
    SERVER_GPT = 'http://127.0.0.1:7000'
