from random import choice
from .openapi import answer as openapi_answer
from .yandexgpt import answer as yandexgpt_answer


async def get_interview(skills, gpt):
    skill = choice(skills)

    if gpt == 'openai':
        answer = await get_openapi_answer(skill)
    else:
        answer = await get_yandex_answer(skill)

    return answer['result']


async def get_interview_answer(question, gpt):
    if gpt == 'openai':
        answer = await get_openapi_answer_to_question(question)
    else:
        answer = await get_yandex_answer_to_question(question)

    return answer['result']


async def get_openapi_answer(skill: str):
    content = f'Я хочу подготовиться к собеседованию на должность python разработчика.  Задай мне вопрос по{skill}'
    return await openapi_answer(content=content)


async def get_yandex_answer(skill: str):
    content = f'Задай мне вопрос по {skill}'
    instruction = 'Я хочу подготовиться к собеседованию на должность python разработчика'

    return await yandexgpt_answer(content=content, instruction=instruction)


async def get_openapi_answer_to_question(question: str):
    return await openapi_answer(content=f'Ответь на вопрос:{question}')


async def get_yandex_answer_to_question(question: str):
    instruction = 'Ответь на вопрос'

    return await yandexgpt_answer(content=question, instruction=instruction)
