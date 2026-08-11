import requests
import dotenv
import os
import json


dotenv.load_dotenv() #it will olad all .env variables in os environmet variable

api_key=os.getenv("google_geminai_api_key")

print(f"api_key:{api_key}")


def get_llm_response():

    # api_endpoint=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    # Streaming endpoint
    api_endpoint = (
            f"https://generativelanguage.googleapis.com/v1beta/"
            f"models/gemini-2.5-flash:streamGenerateContent"
            f"?alt=sse&key={api_key}"
        )
    

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
                      
                      "text": "what is llm how llm work"
                  }
              ]
          },
          
      ]
  }

    headers={
    "content-Type":"application/json"
   }


    res=requests.post(api_endpoint,json=payload,headers=headers,stream=True) #it will make http post request to the geminai server 

    print(f"response:{res}")



    # we want stream response 

    if(res.status_code==200):
          
     # act_res=res.json() # it will wait for complete response that means it will collect all chunks as it come then finally it will return all chunks collectively 


    # we want stream response

     for chunk in res.iter_lines():
        # print(f"chunk without decoding:{chunk}") #when we try to print the chunk we will get it byte format
        # print("\n")

        if(chunk):

            decode_res=chunk.decode("utf-8") # it give data in string format after decoding 
            # print(f"after decoding:{decode_res}") 
            # print("\n")


              

       # remove "data:" prefix
        # if decode_res.startswith("data:"):
        complete_json = decode_res[5:].strip()
        # print("pure json:",complete_json)
        # print("\n")

        # convert json in to dictnary
        dicitnary=json.loads(complete_json)
        # print("dictinary:",dicitnary)
        # print("/n")

        print(f" actual response:{dicitnary["candidates"][0]["content"]["parts"][0]["text"]}")
   
  
    else:
        act_res=res.json()
        print("actual response:",act_res["error"]["message"])

        
get_llm_response()


