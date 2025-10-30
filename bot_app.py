import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("👋 Привет! Бот успешно работает на Railway.")

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Вот список команд: /start, /help, /info")

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("📸 Скачать видео"), KeyboardButton("ℹ️ Помощь"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Выбери действие:", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

    
