from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import Text

from ..parser.new_vacancies import get_new_vacancies
from ..keyboards.inline import get_inline_keyboard, get_gpt_keyboard
from ..utils.state import StepsVacancyID
from ..utils.create_db import add_subscriber, remove_subscriber


async def get_start(message: Message):
    await message.answer(text='Добро пожаловать в чат бот проекта Python Skills Tracker')
    await get_help(message)


async def get_help(message: Message):
    text = '''
    Команды:
    /new - Показать новые вакансии
    /letter - Составить сопроводительное письмо
    /interview - Пройти тестовое собеседование
    /subscribe - Подписаться на рассылку
    /unsubscribe - Отписаться от рассылки
    '''

    await message.answer(text=Text(text).as_markdown())


async def new_vacancies(message: Message):
    new_vacancies_list = await get_new_vacancies()

    if new_vacancies_list:
        for _id, vacancy_text in new_vacancies_list:
            await message.answer(text=vacancy_text,
                                 disable_web_page_preview=True,
                                 reply_markup=get_inline_keyboard(_id),
                                 )
    else:
        await message.answer(text='Пока новых вакансий нет')


async def letter(message: Message, state: FSMContext):
    await state.set_state(StepsVacancyID.GET_VacancyID)
    await state.update_data(_type='letter')
    await message.answer(text='Укажите id вакансии для которой нужно написать сопроводительное письмо')


async def interview(message: Message, state: FSMContext):
    await state.set_state(StepsVacancyID.GET_VacancyID)
    await state.update_data(_type='interview')
    await message.answer(text='Укажите id вакансии по которой вы хотите пройти тестовое собеседование')


async def get_vacancy_id(message: Message, state: FSMContext):
    data = await state.get_data()
    _type = data.get('_type')
    await message.answer(text='Выберите GPT провайдера',
                         reply_markup=get_gpt_keyboard(message.text, _type),
                         )
    await state.clear()


async def subscribe(message: Message):
    await add_subscriber(message.from_user.id)
    await message.answer(text='Подписка оформлена')


async def unsubscribe(message: Message):
    await remove_subscriber(message.from_user.id)
    await message.answer(text='Подписка отменена')
