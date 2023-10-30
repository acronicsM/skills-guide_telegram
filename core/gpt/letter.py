from ..utils.vacancies_utils import remove_html_tags
from .openapi import answer as openapi_answer
from .yandexgpt import answer as yandexgpt_answer


async def get_letter(description, gpt):
    if gpt == 'openai':
        answer = await get_openapi_answer(description)
        return answer['result']

    if gpt == 'yandex':
        answer = await get_yandex_answer(description)
        return answer['result']


async def get_openapi_answer(description: dict):
    description_text = remove_html_tags(description['description'])

    content = f'''
    Я ищу работу и мне нужна помощь в написании сопроводительного письма к вакансии:
    {description_text}
    
    Напиши сопроводительное письмо
    '''

    return await openapi_answer(content=content)


async def get_yandex_answer(description: dict):
    description_text = remove_html_tags(description['description'])

    content = f'Напиши сопровотельное письмо не длиннее 200 символов для вакансии:\n{description_text}'
    instruction = 'Ты состикатель на вакансию'

    return await yandexgpt_answer(content=content, instruction=instruction)


