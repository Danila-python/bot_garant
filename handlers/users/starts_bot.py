from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router
from sqlalchemy.orm import Session


from data.states.local_states import UserData

router = Router()


@router.message(Command(commands=['start']))
async def start_bot(message: Message, state: FSMContext):
    await message.answer(
        'Привет, укажи свой номер телефона для авторизации!'
    )
    await state.clear()
    await state.set_state(UserData.phone)

"""
ДОПИЛИТЬ ПРОВЕРКУ НОМЕРА ТЕЛЕФОНА НА ВАЛИДНОСТЬ!!!!!!!!
"""

# @router.message(UserData.phone)
# async def get_user_phone(message: Message, state: FSMContext, db: Session=):
#     await state.update_data(phone=message.text)

