import requests
import dotenv
import os
import json

dotenv.load_dotenv()

api_key = os.getenv("google_geminai_api_key")

print(f"api_key: {api_key}")


def get_llm_response():

    # Streaming endpoint
    api_endpoint = (
        f"https://generativelanguage.googleapis.com/v1beta/"
        f"models/gemini-2.5-flash:streamGenerateContent"
        f"?alt=sse&key={api_key}"
    )

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {
                        "text": "hi my name is md shahid"
                    }
                ]
            },
            {
                "role": "model",
                "parts": [
                    {
                        "text": "Hi Md Shahid, it's nice to meet you! How can I assist you today?"
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "text": "what is my name?"
                    }
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    # stream=True tells requests to consume the HTTP response progressively
    res = requests.post(
        api_endpoint,
        json=payload,
        headers=headers,
        stream=True
    )

    print(f"response: {res}")

    # Read streaming response
    for chunk in res.iter_lines():

        if chunk:

            # bytes → string
            decode_res = chunk.decode("utf-8")

            print("Decoded:", decode_res)

            # If using SSE, remove "data:" prefix
            if decode_res.startswith("data:"):
                decode_res = decode_res[5:].strip()

            # JSON string → Python dictionary
            dictionary = json.loads(decode_res)

            print("Dictionary:", dictionary)


get_llm_response()