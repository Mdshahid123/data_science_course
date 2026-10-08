# now we have make a api call to llm  and getting stream response 

import requests
import json
# from augmentaion import prompt


def generate_response(prompt):

    api_endpoint = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": True
    }

    response = requests.post(api_endpoint,json=payload,stream=True)
    print(response)

    for line in response.iter_lines():
        if line:
            data = json.loads(line)
            yield data["response"]
            # print(data["response"], end="", flush=True)




