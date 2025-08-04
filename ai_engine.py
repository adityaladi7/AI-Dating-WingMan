import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_ai_message(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()
