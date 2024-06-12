from aiogram import Router, F
from aiogram import Message
from keyboards import keyboards, Animekeyboard, Mangakeyboard

r = Router()


@r.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "топ манги":
        await message.answer( "Воть топ манги:")
    elif msg == "топ аниме":
        await message.answer( "Воть топ аниме:")
    elif msg == "Почитать":
        await message.answer( "Тута можно почитать", reply_markup="")
    elif msg == "Посмотреть":
        await message.answer("Тута можно посмотреть аниме", reply_markup="")
    elif msg == "В главное меню":
        await message.answer("")