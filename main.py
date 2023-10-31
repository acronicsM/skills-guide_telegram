import asyncio
import logging

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler


from settings import Settings
from core.register import routers
from core.handlers import apsched

async def app():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName).s(%(lineno)d) - %(message)s',
                        )

    bot = Bot(token=Settings.API_KEY, parse_mode='MarkdownV2')
    dp = Dispatcher()

    sheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    sheduler.add_job(apsched.send_new_vacancies_cron,
                     trigger='interval',
                     seconds=60,
                     kwargs={'bot': bot})
    sheduler.start()

    routers(dp)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(app())
