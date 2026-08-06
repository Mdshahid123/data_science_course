import requests
from dotenv  import load_dotenv
import os
load_dotenv()
api_key=os.getenv("geminai_api_key") 
print(api_key)



url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

payload= {
    "contents": [
        {
            "parts": [
                {

                    "text": "Hey, how are you?"
                }
            ]
        }
    ]
}

headers={
  "contents_type":"application/json"
}

response=requests.post(url,json=payload,headers=headers)
# print(response)
act_res=response.json()
# print(act_res)

data=act_res["candidates"][0]["content"]["parts"][0]["text"]
print(data)



