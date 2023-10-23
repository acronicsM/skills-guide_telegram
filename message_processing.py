import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv('BOT_API_KEY')

SERVER_ARD = 'http://127.0.0.1:5000'


async def new_vacancies(chat_id):
    uri = f'https://api.telegram.org/bot{TG_API_KEY}/sendMessage'
    params = {'new_vacancies': 'True'}

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{SERVER_ARD}/vacancies', params=params) as response:
            answer = await response.json()

            for i in answer['result']:
                data = {'chat_id': chat_id,
                        'parse_mode': 'MarkdownV2',
                        'text': vacancies_to_text(i)}

                async with session.post(uri, data=data) as response_tg:
                    print(await response_tg.text())
                    print(response_tg.status)

            if not answer['result']:
                data = {'chat_id': chat_id,
                        'parse_mode': 'MarkdownV2',
                        'text': 'Новых вакансий нет'}

                async with session.post(uri, data=data) as response_tg:
                    print(response_tg.status)



def vacancies_to_text(vacancy: dict):
    _id, name, requirement = vacancy['id'], vacancy['name'], vacancy['requirement']
    salary_from = formatted_salary(vacancy["salary_from"], "от")
    salary_to = formatted_salary(vacancy["salary_to"], "до")
    salary = f'{salary_from} {salary_to}'.strip()

    # text = fr'*{name}* \\({_id}\\)'
    # if salary:
    #     text += f'\n{salary}'
    #
    # text += f'\n {requirement}'
    text = f'*{name}*'

    return text


def formatted_salary(salary: float, prefix: str) -> str:
    return f'{prefix} {int(salary):_} ₽'.replace('_', ' ') if salary > 0 else ''
