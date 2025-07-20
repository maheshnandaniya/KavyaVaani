import os
import uuid
from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

def generate_audio(text):
    os.makedirs('media/audio', exist_ok=True)
    filename = f"{uuid.uuid4().hex}.wav"
    filepath = os.path.join('media/audio', filename)
    tts.tts_to_file(text=text, file_path=filepath)
    return f'/media/audio/{filename}'
