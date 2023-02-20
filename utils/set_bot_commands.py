from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeAllPrivateChats
from data.config import admins_id


async def set_default_commands(bot):
    await bot.set_my_commands(
        [
            # BotCommand('start', 'Запустить бота'),
            BotCommand(command='start', description='Запустить бота')
        ],
        scope=BotCommandScopeAllPrivateChats()
    )

    admin_id = int(admins_id[0])

    await bot.set_my_commands(
        [
            # BotCommand('mail', 'Сообщение для рассылки'),
            BotCommand(command='mail', description='Сообщение для рассылки')
        ],
        scope=BotCommandScopeChat(chat_id=admin_id)
    )
