async def on_startup(bot):
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(bot)

    print("Бот запущен!")


async def main():
    from loader import dp, bot

    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio
    from data.db.base import async_session
    from data.db import models
    from data.db.base import async_session

    async_session()

    asyncio.run(main())
