import requests

api_end_point = "http://localhost:11434/api/embed"

payload = {
    "model": "bge-m3",
    "input": "hi my name is md shahid"
}

headers = {
    "Content-Type": "application/json"
}

res = requests.post(
    api_end_point,
    json=payload,
    headers=headers
)

act_res = res.json()

print(act_res)
print(type(act_res))