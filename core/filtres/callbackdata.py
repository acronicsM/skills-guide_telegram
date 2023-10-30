import enum

from aiogram.filters.callback_data import (CallbackData)


class VacancyCall(CallbackData, prefix='vacancy'):
    vacancy_type: str
    vacancy_id: int


class GPT(CallbackData, prefix='gpt'):
    gpt_provider: str
    vacancy_type: str
    vacancy_id: int | str


class InterviewAnswer(CallbackData, prefix='interview'):
    gpt_provider: str
    question: str
