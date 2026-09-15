import requests
from config import EMBEDDING_MODEL, EMBEDDING_URL


def create_embedding(text):

    payload = {
        "model": EMBEDDING_MODEL,
        "input": text
    }

    response = requests.post(
        EMBEDDING_URL,
        json=payload
    )

    response.raise_for_status()

    actual_response = response.json()

    return actual_response["embeddings"][0]