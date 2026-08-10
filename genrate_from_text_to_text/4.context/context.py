import requests
import dotenv
import os


dotenv.load_dotenv() #it will olad all .env variables in os environmet variable

api_key=os.getenv("google_geminai_api_key")

print(api_key)


def get_llm_response():
    api_endpoint=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    payload={
      "contents": [
          {
              "role":"user",
              "parts": [
                  {
                      
                      "text": "hi my name is md shahid"
                  }
              ]
          },
          {
              "role":"model",
              "parts": [
                  {
                      
                      "text": "Hi Md Shahid, it's nice to meet you! How can I assist you today?"
                  }
              ]
          },
          
          {
              "role":"user",
              "parts": [
                  {
                      
                      "text": "what is my name "
                  }
              ]
          },
          
      ]
  }

    headers={
    "contents_type":"application/json"
   }


    res=requests.post(api_endpoint,json=payload,headers=headers)#it will make http post request to the geminai server 
    print(res)

    act_res=res.json()
   
    if(res.status_code==200):
        print(act_res["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print(act_res["error"]["message"])
        
get_llm_response()


