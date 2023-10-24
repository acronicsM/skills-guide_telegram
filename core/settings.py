import os

from dotenv import load_dotenv

from .handlers.basic import new_vacancies, letter, interview

load_dotenv()

API_KEY = os.getenv('BOT_API_KEY')

COMMANDS = {
    'new': {
        'name': 'Новые вакансии',
        'description': 'Показать новые вакансии',
        'function': new_vacancies,
    },
    'letter': {
        'name': 'Cопроводительное письмо',
        'description': 'Составить сопроводительное письмо',
        'function': letter,
    },
    'interview': {
        'name': 'Тестовое собеседование',
        'description': 'Пройти тестовое собеседование',
        'function': interview,
    },
    'subscribe': {
        'name': 'Подписаться',
        'description': 'Подписаться на рассылку',
        'function': interview,
    },
    'unsubscribe': {
        'name': 'Отписаться',
        'description': 'Отписаться от рассылки',
        'function': interview,
    },
}

SERVER_PARSE = 'http://127.0.0.1:5000'
