from datetime import datetime, timedelta

from aiogram import Bot

from settings import Settings
from ..utils.create_db import all_subscribers
from ..parser.new_vacancies import get_new_vacancies
from ..keyboards.inline import get_inline_keyboard


async def send_new_vacancies_cron(bot: Bot):
    new_date = datetime.now() - timedelta(seconds=Settings.NEW_VACANCIES_CRON_PERIOD)

    new_vacancies_list = await get_new_vacancies(new_date)

    if new_vacancies_list:
        subscribers = await all_subscribers()
        for subscriber in subscribers:
            for _id, vacancy_text in new_vacancies_list:
                await bot.send_message(subscriber.id,
                                       text=vacancy_text,
                                       disable_web_page_preview=True,
                                       reply_markup=get_inline_keyboard(_id),
                                       )
