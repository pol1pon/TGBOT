from aiogram import Router
from aiogram import Commnads, CommandStart, CommandsObject
from aiogram.types import Message
from keyboards import keyboards

r = Router()

@r.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветик, это Манга бот", reply_markup=keyboards.main)

@r.message(CommandsObject.text=="/help")
async def help(message: Message):
    await message.answer(f"Воть список Слов которые воспринимает бот", ) #Надо дописать список команд