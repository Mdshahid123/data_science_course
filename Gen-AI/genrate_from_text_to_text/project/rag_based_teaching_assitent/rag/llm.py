import requests

from config import LLM_MODEL, GENERATE_URL


def generate_answer(prompt):

    payload = {
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        GENERATE_URL,
        json=payload
    )

    response.raise_for_status()

    actual_response = response.json()

    return actual_response["response"]