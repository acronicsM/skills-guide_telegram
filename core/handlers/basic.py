from aiogram.types import Message

from settings import Settings
from .new_vacancies import get_new_vacancies
from ..keyboards.inline import get_inline_keyboard


async def get_start(message: Message):
    await message.answer(text='Добро пожаловать в чат бот проекта Python Skills Tracker')
    await get_help(message)


async def get_help(message: Message):
    text = '\n'.join(f'/{k} \- {v["description"]}' for k, v in Settings.COMMANDS.items())
    await message.answer(text=f'Команды:\n{text}')


async def new_vacancies(message: Message):
    new_vacancies_list = await get_new_vacancies()
    for _id, vacancy_text in new_vacancies_list:
        await message.answer(text=vacancy_text,
                             disable_web_page_preview=True,
                             reply_markup=get_inline_keyboard(_id),
                             )


async def letter(message: Message):
    await message.answer(text='Сопроводительное письмо')


async def interview(message: Message):
    await message.answer(text='Тестовое собеседование')
