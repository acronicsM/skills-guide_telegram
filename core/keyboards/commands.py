from aiogram import Bot
from aiogram.types import BotCommand

from core import settings


async def setup_bot_commands(bot: Bot):
    bot_commands = [BotCommand(command=f'/{k}', description=v['name']) for k, v in settings.COMMANDS.items()]

    await bot.set_my_commands(bot_commands)
