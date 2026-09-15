import requests
from dotenv  import load_dotenv
import os
load_dotenv()
api_key=os.getenv("geminai_api_key") 
print(api_key)

# we have defined the invoke llm function
history=[]
def invoke_llm(prompt):
  url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

# Add user's message
  history.append({
        "role": "user",
        "parts": [
            {
                "text": prompt
            }
        ]
    })


  payload= {
      "contents": history
    }

  headers={
    "contents_type":"application/json"
  }

  response=requests.post(url,json=payload,headers=headers)
  # print(response)
  act_res=response.json()


  # print(act_res)

  data=act_res["candidates"][0]["content"]["parts"][0]["text"]
  # Save Gemini's response
  history.append({
        "role": "model",
        "parts": [
            {
                "text": data
            }
        ]
    })
  return data







