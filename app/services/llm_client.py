import requests

def ask_llm(prompt: str) -> str:
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload, timeout=120)
    response.raise_for_status()

    return response.json()["response"]