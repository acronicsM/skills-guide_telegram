from aiogram.fsm.state import StatesGroup, State


class StepsVacancyID(StatesGroup):
    GET_VacancyID = State()


class StepsInterview(StatesGroup):
    Step_question = State()
