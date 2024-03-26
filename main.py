import os
import asyncio
import logging
from pathlib import Path

import aiogram.methods.send_voice
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from sim_project.tts import SimlishTTS
from sim_project.gpt_translate import SimlishTranslate


bot = Bot(token=os.environ["BOT_API"])
dp = Dispatcher()

translate = SimlishTranslate()
audio = SimlishTTS(speaker_promt_path="female_voice.mp3", save_path="/home/ekh/SimProject/sim_project/", )
@dp.message()
async def cmd_start(message: types.Message):
    translate_answer = translate(message.text)
    audio_file_path = audio.generate(text=translate_answer)



    voice = types.input_file.InputFile(audio_file_path)
    #audio_file = types.input_file.InputFile(filenam  e=audio_file_path)
    with open(audio_file_path, 'rb') as audio_file:
        await bot.send_voice(chat_id=message.chat.id, voice=voice)

    #await message.answer_voice(voice=voice)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())