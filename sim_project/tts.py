import uuid
from TTS.api import TTS

class SimlishTTS:
    def __init__(self, speaker_promt_path: str, save_path: str):
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda:0")
        self.speaker_promt_path = speaker_promt_path
        self.save_path = save_path

    def generate(self, text: str):
        file_name = self.save_path + "/" + str(uuid.uuid4()) + '.wav'
        audio = self.tts.tts_to_file(text=text,
                file_path=file_name,
                speaker_wav=self.speaker_promt_path,
                language="en")
        return file_name