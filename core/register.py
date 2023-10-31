from aiogram.filters import Command

from .handlers import basic
from .handlers.callback import select_letter, select_gpt, answer_question
from .filtres.callbackdata import VacancyCall, GPT

from .utils.state import StepsVacancyID, StepsInterview

def routers(dp):

    dp.callback_query.register(select_letter, VacancyCall.filter())
    dp.callback_query.register(select_gpt, GPT.filter())
    dp.callback_query.register(answer_question, StepsInterview.Step_question)

    dp.message.register(basic.get_start, Command(commands=['start']))
    dp.message.register(basic.get_help, Command(commands=['help']))
    dp.message.register(basic.new_vacancies, Command(commands=['new']))
    dp.message.register(basic.letter, Command(commands=['letter']))
    dp.message.register(basic.interview, Command(commands=['interview']))
    dp.message.register(basic.subscribe, Command(commands=['subscribe']))
    dp.message.register(basic.unsubscribe, Command(commands=['unsubscribe']))

    dp.message.register(basic.get_vacancy_id, StepsVacancyID.GET_VacancyID)
