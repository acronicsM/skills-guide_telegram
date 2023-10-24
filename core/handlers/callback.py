from aiogram import Bot
from aiogram.types import CallbackQuery

from core.filtres.callbackdata import VacancyCall


async def select_letter(call: CallbackQuery, bot: Bot, callback_data: VacancyCall):
    _id, _type = callback_data.vacancy_id, callback_data.vacancy_type

    answer = 'Неопознано'

    if _type == 'letter':
        answer = f'Сопроводительное письмо для вакансии {_id}'
    elif _type == 'interview':
        answer = f'Тестовое собеседование для вакансии {_id}'


    # _, _id = call.data.split('_')
    # answer = f'Сопроводительное письмо для вакансии {_id}'
    #
    await call.message.answer(answer)
    await call.answer()


async def select_interview(call: CallbackQuery, bot: Bot):
    _, _id = call.data.split('_')
    answer = f'Тестовое собеседование для вакансии {_id}'

    await call.message.answer(answer)
    await call.answer()
