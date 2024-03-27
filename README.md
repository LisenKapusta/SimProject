## Simlish Translator

### Installation
```bash
git clone  https://github.com/LisenKapusta/SimProject.git
```

pip install .

#### Overview

GPT-Based translation to Simlish language in telegram bot
#### Project Components

1. Bot:
   - Implementation: The aiogram library is used for message handling. Incoming text messages are translated into Simlish using the SimlishTranslate component, then the Simlish text is converted into speech via SimlishTTS, and the resulting audio file is sent to the user.

2. Text to Speech:
   - Implementation: The SimlishTTS class is created, utilizing a TTS (text-to-speech) API to convert text into audio. Audio files are saved with unique names to prevent conflicts and overwriting.

3. Simlish Translation:
   - Implementation: GPT from OpenAI is used to generate translations based on predefined rules and examples of Simlish. The SimlishTranslate class handles translation requests and returns text in Simlish.

#### Technology Stack

- aiogram: For creating and managing the Telegram bot.
- librosa and scipy: For processing audio files (e.g., noise reduction).
- soundfile: For saving processed audio files.
- OpenAI API: For generating translations into Simlish.

#### Usage
1. Install repository
2. Export OpenAI API Key & Telegram bot API Key
3. 
```bash
export OPENAI_API_KEY="your_token"
export BOT_API="your_token"
```
3. Run bot
```bash
python main.py
```
