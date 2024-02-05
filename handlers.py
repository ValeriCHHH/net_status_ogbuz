from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer('Hi! I am know your ID. Tell for you?')

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f'Your ID: {msg.from_user.id}')