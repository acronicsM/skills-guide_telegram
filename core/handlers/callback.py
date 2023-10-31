from aiogram import Bot
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import Text
from aiogram.fsm.context import FSMContext

from .basic import get_help
from ..filtres.callbackdata import VacancyCall, GPT
from ..keyboards.inline import get_gpt_keyboard, get_interview_keyboard
from ..gpt.letter import get_letter
from ..gpt.interview import get_interview, get_interview_answer
from ..parser.description_vacancy import get_description
from ..utils.state import StepsInterview


async def select_letter(call: CallbackQuery, callback_data: VacancyCall):
    _id, _type = callback_data.vacancy_id, callback_data.vacancy_type

    await call.message.answer(text='Выберите GPT провайдера',
                              reply_markup=get_gpt_keyboard(_id, _type),
                              )


async def select_gpt(call: CallbackQuery, callback_data: GPT, state: FSMContext):
    _id, _type, gpt = callback_data.vacancy_id, callback_data.vacancy_type, callback_data.gpt_provider

    description = await get_description(_id)

    if not description:
        await call.message.answer(Text(f'Не удалось загрузить описание вакансии {_id}').as_markdown())
    elif _type == 'letter':
        answer = await get_letter(description, gpt)
        await call.message.answer(text=Text(answer).as_markdown())
    else:
        skills = description['key_skills'] + description['basic_skills']
        await state.update_data(skills=skills)

        answer = await get_interview(skills, gpt)
        await state.set_state(StepsInterview.Step_question)
        await state.update_data(answer=answer)

        await call.message.answer(text=Text(answer).as_markdown(),
                                  reply_markup=get_interview_keyboard(gpt=gpt),
                                  )

    await call.answer()


async def answer_question(call: CallbackQuery, state: FSMContext):
    _, gpt, is_answer, is_exit = call.data.split(':')
    is_answer, is_exit = bool(int(is_answer)), bool(int(is_exit))

    data = await state.get_data()

    if is_exit:
        await get_help(call.message)
        await state.clear()
    elif is_answer:
        answer = await get_interview_answer(data.get('answer'), gpt)
        await state.update_data(answer=None)

        await call.message.answer(text=Text(answer).as_markdown(),
                                  reply_markup=get_interview_keyboard(gpt=gpt, with_answer=False),
                                  )
    else:
        answer = await get_interview(data.get('skills'), gpt)
        await state.update_data(answer=answer)

        await call.message.answer(text=Text(answer).as_markdown(),
                                  reply_markup=get_interview_keyboard(gpt=gpt),
                                  )

    await call.answer()
