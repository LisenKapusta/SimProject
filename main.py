import os
import asyncio
import logging

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
    #audio_file = types.voice.Voice(file_id=audio_file_path)

    audio_file = types.input_file.InputFile(filename=audio_file_path)
    #file = types.audio.Audio(file_name=audio_file)
    #audio_file = types.document.Document(file_id=audio_file_path)
    #with open(audio_file_path, mode="rb") as file:
        #binary_content = file.read()
    #await message.answer_voice(voice=binary_content, caption="Ваше сообщение на симлише:")
    #message.reply(binary_content)
    #await aiogram.methods.send_voice.SendVoice(voice=file)
    await message.answer_voice(audio_file)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())