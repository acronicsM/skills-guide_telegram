from aiogram import Bot
from aiogram.types import BotCommand

from settings import Settings
from ..handlers.basic import new_vacancies, letter, interview


async def setup_bot_commands(bot: Bot):
    bot_commands = [BotCommand(command=f'/{k}', description=v['name']) for k, v in Settings.COMMANDS.items()]

    await bot.set_my_commands(bot_commands)


def get_commands():
    return {
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
