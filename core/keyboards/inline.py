from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.filtres.callbackdata import VacancyCall


def get_inline_keyboard(_id):
    builder = InlineKeyboardBuilder()
    builder.button(text='✉️ Сопров...', callback_data=VacancyCall(vacancy_type='letter', vacancy_id=_id))
    builder.button(text='📝 Собес...', callback_data=VacancyCall(vacancy_type='interview', vacancy_id=_id))

    return builder.as_markup()
