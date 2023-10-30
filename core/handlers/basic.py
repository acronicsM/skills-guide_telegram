from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from settings import Settings
from ..parser.new_vacancies import get_new_vacancies
from ..keyboards.inline import get_inline_keyboard, get_gpt_keyboard
from ..utils.state import StepsVacancyID


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


async def letter(message: Message, state: FSMContext):
    await message.answer(text='Укажите id вакансии для которой нужно написать сопроводительное письмо')
    await state.set_state(StepsVacancyID.GET_VacancyID)


async def interview(message: Message):
    await message.answer(text='Тестовое собеседование')


async def get_vacancy_id(message: Message, state: FSMContext):
    await message.answer(text='Выберите GPT провайдера',
                         reply_markup=get_gpt_keyboard(message.text, 'letter'),
                         )
    await state.clear()
