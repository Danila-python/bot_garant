from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router

from data.config import admins_id

router = Router()


@router.message(Command(commands=['start']))
async def start_bot(message: Message):
    await message.answer(
        'Привет, ты успешно авторизован!'
    )
