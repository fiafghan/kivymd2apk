import openai
from API import API

your_openai_key = API

def talk(text):
    client = openai.OpenAI(api_key=your_openai_key)

    response = client.audio.speech.create(
    model="tts-1",
    voice="onyx", # other voices: 'echo', 'fable', 'onyx', 'nova', 'shimmer'
    input=text
    )

    response.stream_to_file('computer_generated_speech.mp3')

    client.close()