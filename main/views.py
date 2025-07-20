import os
from django.shortcuts import render
from dotenv import load_dotenv
import openai
from .tts_engine import generate_audio

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def index(request):
    return render(request, 'index.html')

def generate_poem(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a poet. Respond only with poems."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300
            )
            poem = response['choices'][0]['message']['content'].strip()
            audio_path = generate_audio(poem)  # Generate audio
            return render(request, 'result.html', {
                'poem': poem,
                'audio_path': audio_path
            })
        except Exception as e:
            return render(request, 'result.html', {
                'error': str(e)
            })
