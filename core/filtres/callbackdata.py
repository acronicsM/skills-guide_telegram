from aiogram.filters.callback_data import (CallbackData)


class VacancyCall(CallbackData, prefix='vacancy'):
    vacancy_type: str
    vacancy_id: int
