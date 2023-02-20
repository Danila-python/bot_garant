from aiogram.fsm.state import StatesGroup, State


class Mail(StatesGroup):
    mail = State()


class UserData(StatesGroup):
    phone = State()
