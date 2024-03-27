import os
import asyncio
import aiogram.methods.send_voice
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import librosa
import numpy as np
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf


from sim_project.tts import SimlishTTS
from sim_project.gpt_translate import SimlishTranslate


bot = Bot(token=os.environ["BOT_API"])
dp = Dispatcher()

translate = SimlishTranslate()
audio = SimlishTTS(speaker_promt_path="female_voice.mp3", save_path="./tts_cache/, )
@dp.message()
async def echo_voice(message: types.Message):
    translate_answer = translate(message.text)
    audio_file_path = audio.generate(text=translate_answer)
    y, sr = librosa.load(audio_file_path, sr=None)

    reduced_noise_stationary = nr.reduce_noise(y=y, y_noise=None, sr=sr, n_std_thresh_stationary=1.5,
                                               stationary=False)
    sf.write('cleaned_audio_file_stationary.wav', reduced_noise_stationary, sr)
    voice_file = types.FSInputFile('cleaned_audio_file_stationary.wav')
    await message.answer_voice(voice_file)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())