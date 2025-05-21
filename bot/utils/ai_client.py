import requests
from .config import OLLAMA_URL

def chat_with_ai(messages):
    url = f"{OLLAMA_URL}/api/chat"
    data = {
        "model": "llama3",
        "messages": messages,
        "stream": False
    }
    r = requests.post(url, json=data)
    r.raise_for_status()
    return r.json()["message"]["content"]
