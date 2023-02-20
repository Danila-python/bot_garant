from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from data.config import admins_id
from data.states.mail_states import Mail
from data.config import clients_id

from utils.midlware.midlware_admin import AdminMessageMiddleware

router = Router()
router.message.middleware(AdminMessageMiddleware())


# @router.message(Command(commands=['mail']), F.chat.func(lambda chat: chat.id in admins_id))
@router.message(Command(commands=['mail']))
async def start_spam(message: Message, state: FSMContext):
    await message.answer(
        '<b>Отправьте сообщение для рассылки:</b>'
    )
    await state.clear()
    await state.set_state(Mail.mail)


# @router.message(Mail.mail, F.chat.func(lambda chat: chat.id in admins_id))
@router.message(Mail.mail)
async def spam(message: Message, state: FSMContext):
    await state.update_data(mail=message.text)
    for id in clients_id:
        try:
            await message.copy_to(
                chat_id=id,
            )
        except Exception as e:
            print("Логи потом как-нибудь подключу")
            print(e)
    await state.clear()
