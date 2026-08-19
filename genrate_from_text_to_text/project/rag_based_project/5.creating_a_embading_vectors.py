
import os   # internal module
import json # internal moldule
import requests


# let's define the create embadding function 

def create_embedding(text):

    # to createa embedding for the given text we have to createe embedding 
    # for this we have to make a api call to the ollma server at localhost: /api/embed
    api_end_point="http://localhost:11434/api/embed"
    payload={
       "model":" bge-m3",
       "input":text
    }


    headers={
       "Contents-Type":"application/json"
    }
    res=requests.post(api_end_point,json=payload,headers=headers)
    print(res)
    act_res=res.json()
    print(act_res)


# step-01 ecess all json files one by one thorugh the loop

json_files=os.listdir("json")  # it will return the list of file 
count1=1
for file in json_files:
  if(count1==2):
     break

  file=open(f"json/{file}","r")
  json_fomrat=file.read()
  dictinary_format=json.loads(json_fomrat) #it will convert(parse) the json_fomat into the it's orginal fomrat(in this case we have a dictinalry is a original format)
  count1=count1+1

#   we have to ftech the text or chunks form the current file and then for that we have create a embadding 
  count2=1
  for chunk in dictinary_format["segements"]:
    if(count2==2):
       break
    text=chunk["text"]
    create_embedding(text)
    count2=count2+1



    


  
   
