from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram import Router
from sqlalchemy.orm import Session

from data.db.base import get_session, Users as UsersDb

from data.states.local_states import UserData

router = Router()


@router.message(Command(commands=['start']))
async def start_bot(message: Message, state: FSMContext):
    await message.answer(
        'Привет, укажи свой email для авторизации!'
    )
    await state.clear()
    await state.set_state(UserData.email)

"""
ДОПИЛИТЬ ПРОВЕРКУ НОМЕРА ТЕЛЕФОНА НА ВАЛИДНОСТЬ!!!!!!!!
"""


@router.message(UserData.email)
async def get_user_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    async with get_session() as session:
        if session.query(UsersDb).filter_by(user_id=str(message.from_user.id)).first() is not None:
            await message.answer(
                'Вы уже зарегистрированны'
            )

        else:
            if type(message.text) is int:
                user_db = UsersDb(
                    user_id=str(message.from_user.id),
                    user_mobile_phone=str(message.text)
                )
                try:
                    session.add(user_db)
                    await session.commit()
                    await message.answer(
                        'Вы успешно зарегистрированны!'
                    )

                except Exception as ex:
                    print(ex)

            else:
                await message.answer(
                    'Вы не прошли валидацию'
                )

