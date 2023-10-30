import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from settings import Settings
from core.handlers.basic import get_start, get_help, get_vacancy_id
from core.handlers.callback import select_letter, select_gpt
from core.filtres.callbackdata import VacancyCall, GPT
from core.keyboards.commands import setup_bot_commands, get_commands

from core.utils.state import StepsVacancyID


async def start_bot(bot: Bot):
    await setup_bot_commands(bot)


async def app():

    Settings.COMMANDS = get_commands()

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName).s(%(lineno)d) - %(message)s',
                        )

    bot = Bot(token=Settings.API_KEY, parse_mode='MarkdownV2')
    dp = Dispatcher()

    for k, v in Settings.COMMANDS.items():
        dp.message.register(v['function'], Command(commands=[k]))

    dp.callback_query.register(select_letter, VacancyCall.filter())
    dp.callback_query.register(select_gpt, GPT.filter())

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))

    dp.message.register(get_vacancy_id, StepsVacancyID.GET_VacancyID)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(app())
