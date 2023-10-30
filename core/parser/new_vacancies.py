import aiohttp

from aiogram.utils.formatting import Text
from aiogram.utils.markdown import link, bold

from settings import Settings

from ..utils.vacancies_utils import remove_html_tags


async def get_new_vacancies():
    params = {'new_vacancies': 'True'}

    async with aiohttp.ClientSession() as session:
        async with session.get(f'{Settings.SERVER_PARSE}/vacancies', params=params) as response:
            answer = await response.json()

            return [vacancy_to_tuple(i) for i in answer['result']]


def vacancy_to_tuple(vacancy: dict):
    _id, url, name, requirement = vacancy['id'], vacancy['url'], vacancy['name'], vacancy['requirement']
    salary_from, salary_to = vacancy["salary_from"], vacancy["salary_to"]

    return _id, vacancy_to_text(_id, name, url, requirement, salary_from, salary_to)


def vacancy_to_text(_id: int, name: str, url: str, requirement: str, salary_from: float, salary_to: float):
    _id, name, requirement = link(str(_id), url), bold(name), Text(remove_html_tags(requirement)).as_markdown()

    if salary := f'{formatted_salary(salary_from, "от")} {formatted_salary(salary_to, "до")}'.strip():
        salary = f'\n{salary}'

    return f'{name}\n{_id}{salary}\n{requirement}'


def formatted_salary(salary: float, prefix: str) -> str:
    return f'{prefix} {int(salary):_} ₽'.replace('_', ' ') if salary > 0 else ''
