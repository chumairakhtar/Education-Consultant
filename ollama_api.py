import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"   # installed model

def fetch_ollama_suggestion(prompt, delay_seconds=2):
    """Send a prompt to local Ollama model and return AI suggestion."""
    time.sleep(delay_seconds)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        data = response.json()
        return data.get("response", "No response from Ollama.")

    except requests.exceptions.RequestException as e:
        return f"Ollama connection error: {e}"

    except Exception as e:
        return f"Unexpected error: {e}"
