import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Hello!")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())