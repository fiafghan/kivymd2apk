from openai import OpenAI
from API import API


def get_info_from_openai(text):
    client = OpenAI(api_key=API)

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"explain {text} in very simple words for a 10 up to 15 years old child in Persian."}
    ]
    )
    text = completion.choices[0].message.content
    return text
