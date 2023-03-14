from aiogram.fsm.state import StatesGroup, State


class Mail(StatesGroup):
    mail = State()


class UserData(StatesGroup):
    email = State()
