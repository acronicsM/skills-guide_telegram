import json

import aiohttp

from settings import Settings


async def answer(content: str):

    data = {
        'content': content,
        'model': None,
        'provider': 'Default'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url=f'{Settings.SERVER_GPT}/chatgpt/answer',
                                data=json.dumps(data),
                                headers={"Content-Type": "application/json"}
                                ) as response:
            if response.status == 200:
                return await response.json()

            return {'result': 'Не удалось получить ответ от GPT модели'}