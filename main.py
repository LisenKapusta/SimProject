import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from sim_project.tts import SimlishTTS
from sim_project.gpt_translate import SimlishTranslate


bot = Bot(token=os.environ["BOT_API"])
dp = Dispatcher()

translate_answer = SimlishTranslate()
@dp.message()
async def cmd_start(message: types.Message):
    await message.answer(translate_answer(message))
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())