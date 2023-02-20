from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import users, admin

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode='html')

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(users.router)
dp.include_router(admin.router)
