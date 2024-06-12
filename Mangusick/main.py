import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand
from keyboards import keyboards, Animekeyboard, Mangakeyboard


# Токен бота и диспечер
bot = Bot("")
dp = Dispatcher()


# Ответ на /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Приветик, это Аниме\Манга бот", reply_markup=keyboards.main)




@dp.message()
async def echo(message: Message):
    msg = message.text.lower()

    if msg == "топ манги":
        await message.answer( "Воть топ манги:", reply_markup=Mangakeyboard.Zalypa)
    elif msg == "топ аниме":
        await message.answer( "Воть топ аниме:", reply_markup=Animekeyboard.Xyeta)
    elif msg == "читать мангу":
        await message.answer( "Тута можно почитать", reply_markup=Mangakeyboard.ReadButton)
    elif msg == "смотреть аниме":
        await message.answer("Тута можно посмотреть аниме", reply_markup=Animekeyboard.WatchButton)
    elif msg == "найти мангу/аниме":
        await message.answer("Напишите название Манги/Аниме которое хотите найти")


    else:
        await message.answer("Обучалка", reply_markup=keyboards.meme)
    

# Включение этого ебаного куска говна
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print("Bot robitaet, vse zaebis")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

