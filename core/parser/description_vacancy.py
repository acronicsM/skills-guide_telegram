import aiohttp

from settings import Settings


async def get_description(_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{Settings.SERVER_PARSE}/vacancies/description/{_id}') as response:
            if response.status == 200:
                return await response.json()

    return dict()
