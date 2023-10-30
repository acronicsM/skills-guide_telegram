from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import Text

from ..filtres.callbackdata import VacancyCall, GPT, InterviewAnswer
from ..keyboards.inline import get_gpt_keyboard, get_interview_keyboard
from ..gpt.letter import get_letter
from ..gpt.interview import get_interview
from ..parser.description_vacancy import get_description


async def select_letter(call: CallbackQuery, bot: Bot, callback_data: VacancyCall):
    _id, _type = callback_data.vacancy_id, callback_data.vacancy_type

    await call.message.answer(text='Выберите GPT провайдера',
                              reply_markup=get_gpt_keyboard(_id, _type),
                              )


async def select_gpt(call: CallbackQuery, bot: Bot, callback_data: GPT):
    _id, _type, gpt = callback_data.vacancy_id, callback_data.vacancy_type, callback_data.gpt_provider

    description = await get_description(_id)

    if not description:
        await call.message.answer(Text(f'Не удалось загрузить описание вакансии {_id}').as_markdown())
    elif _type == 'letter':
        answer = await get_letter(description, gpt)
        await call.message.answer(text=Text(answer).as_markdown())
    else:
        answer = await get_interview(description, gpt)
        await call.message.answer(text=Text(answer).as_markdown(),
                                  reply_markup=get_interview_keyboard(gpt=gpt, question=answer),
                                  )

    await call.answer()


async def select_interview_(call: CallbackQuery, bot: Bot, callback_data: InterviewAnswer):
    question, gpt = callback_data.question, callback_data.gpt_provider

    await call.message.answer(text=Text('213213213').as_markdown(),
                              )
    await call.answer()
