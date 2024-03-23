print("Hello")
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token="...")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")
