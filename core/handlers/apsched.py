from aiogram import Bot

from ..utils.create_db import all_subscribers


async def send_new_vacancies_cron(bot: Bot):
    subscribers = await all_subscribers()
    for subscriber in subscribers:
        await bot.send_message(subscriber.id, 'тест')
