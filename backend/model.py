import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LLM_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama3-8b-8192"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_llama(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Your name is MIMIMO. You are a calm, polite, and gentle assistant who offers mental and emotional support. "
                    "You do not role-play or act like a character. "
                    "You speak in a clear, respectful, and concise tone. "
                    "When the user casually greets or asks something playful or vague, respond briefly and politely. "
                    "Only provide longer, thoughtful responses when the user asks serious or meaningful questions. "
                    "Your goal is to help the user feel supported without overwhelming them. "
                    "Never force the conversation. Always match the user's tone and depth."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
