import os

import aiohttp
from dotenv import load_dotenv

load_dotenv()

TG_API_KEY = os.getenv('BOT_API_KEY')

SERVER_ARD = 'http://127.0.0.1:5000'


async def new_vacancies(chat_id):
    params = {'new_vacancies': 'True'}

    # async with aiohttp.ClientSession() as session:
    #     async with session.post(f'https://api.telegram.org/bot{TG_API_KEY}/sendMessage', data=data) as response:
    #         print(response.status)

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{SERVER_ARD}/vacancies', params=params) as response:
            answer = await response.json()
            vacancies_list = [vacancies_to_text(i) for i in answer['result']]
            text_tg = '\n'.join(vacancies_list)

            data = {
                'chat_id': chat_id,
                'text': text_tg,
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(f'https://api.telegram.org/bot{TG_API_KEY}/sendMessage', data=data) as response:
                    print(response.status)


def vacancies_to_text(vacancy: dict):
    text = f'''
    {vacancy['id']}
    {vacancy['name']}
    {formatted_salary(vacancy["salary_from"], "от ")} {formatted_salary(vacancy["salary_from"], " до")}
    {vacancy['requirement']}   
    '''

    return text

def formatted_salary(salary: float, prefix: str) -> str:
    return f'{prefix} {int(salary):_} ₽'.replace('_', ' ') if salary > 0 else ''
