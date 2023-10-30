from random import choice
from .openapi import answer as openapi_answer
from .yandexgpt import answer as yandexgpt_answer


async def get_interview(description, gpt):
    skill = choice(description['key_skills'] + description['basic_skills'])

    if gpt == 'openai':
        answer = await get_openapi_answer(skill)
        return answer['result']

    if gpt == 'yandex':
        answer = await get_yandex_answer(skill)
        return answer['result']


async def get_openapi_answer(skill: str):
    return await openapi_answer(content=f'Придумай вопрос для технического интервью по {skill}')


async def get_yandex_answer(skill: str):
    content = f'Придумай вопрос по {skill}'
    instruction = 'Ты тимлид проводящий собеседование'

    return await yandexgpt_answer(content=content, instruction=instruction)
