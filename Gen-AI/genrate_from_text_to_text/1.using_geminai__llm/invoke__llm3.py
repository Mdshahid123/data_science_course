import requests
from dotenv  import load_dotenv
import os
load_dotenv()
api_key=os.getenv("geminai_api_key") 
print(api_key)

# we have defined the invoke llm function

def invoke__llm(prompt):
  url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

  payload= {
      "contents": [
          {
              "parts": [
                  {

                      "text": prompt
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
  return data







