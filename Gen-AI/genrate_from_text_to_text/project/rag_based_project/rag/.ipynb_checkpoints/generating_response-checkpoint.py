# now we have make a api call to llm ()

import requests
from augmentaion import prompt
api_endpoint = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
}

response = requests.post(api_endpoint,json=payload)
print(response)

actual_response = response.json()
# print(actual_response)

answer = actual_response['response']

print("Answer:",answer)
