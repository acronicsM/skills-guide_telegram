from aiogram.utils.keyboard import InlineKeyboardBuilder

from core.filtres.callbackdata import VacancyCall, GPT, InterviewAnswer


def get_inline_keyboard(_id):
    builder = InlineKeyboardBuilder()
    builder.button(text='✉️ Сопров...', callback_data=VacancyCall(vacancy_type='letter', vacancy_id=_id))
    builder.button(text='📝 Собес...', callback_data=VacancyCall(vacancy_type='interview', vacancy_id=_id))

    return builder.as_markup()


def get_gpt_keyboard(_id, _type):
    builder = InlineKeyboardBuilder()
    builder.button(text='Yandex', callback_data=GPT(gpt_provider='yandex',
                                                    vacancy_type=_type,
                                                    vacancy_id=_id,
                                                    ),
                   )

    builder.button(text='ChatGPT', callback_data=GPT(gpt_provider='openai',
                                                     vacancy_type=_type,
                                                     vacancy_id=_id,
                                                     ),
                   )

    return builder.as_markup()


def get_interview_keyboard(gpt, with_answer=True):
    builder = InlineKeyboardBuilder()

    if with_answer:
        builder.button(text='🔑 Ответ', callback_data=InterviewAnswer(gpt_provider=gpt, answer=True, exit=False))

    builder.button(text='🧰 Еще', callback_data=InterviewAnswer(gpt_provider=gpt, answer=False, exit=False))
    builder.button(text='❌ Хватит', callback_data=InterviewAnswer(gpt_provider=gpt, answer=False, exit=True))

    return builder.as_markup()
