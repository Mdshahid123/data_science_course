import requests
import os
import dotenv


dotenv.load_dotenv() #it will load the all variables insdoe a .env file to envirronment variable of os


api_key=os.getenv("deep_seek_api_key") #it will exccess the deep_seek_api_key variable from os environmentl variable
print(api_key)

def get_response_from_deepSeek_llm(prompt):
  api_end_point="https://api.deepseek.com/chat/completions"
  payload= {
      "model": "deepseek-chat",
      "messages": [
          {
              "role": "user",
              "content":prompt 
          }
      ],
      "temperature": 0.7,
      "max_tokens": 1024
  }

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

  response=requests.post(api_end_point,json=payload,headers=headers)
  print(response)
  act_res=response.json()
  print(act_res)
  if(response.status_code==200):
    print(act_res["choices"][0]["message"]["content"])
  print(act_res["error"]["message"])


get_response_from_deepSeek_llm("hi")



