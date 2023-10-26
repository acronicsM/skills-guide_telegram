import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    API_KEY = os.getenv('BOT_API_KEY')

    SERVER_PARSE = 'http://127.0.0.1:5000'
    GPT_ADDR = 'http://127.0.0.1:7000/gpt'

    COMMANDS = dict()
