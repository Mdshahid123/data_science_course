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
    act_res=res.json()
    return  act_res["embeddings"][0]
    

def give_all_jason_files():
 
 json_files=os.listdir("json")  # it will return the list of file 
 return json_files


def read_json_file_content(folderName,fileName):
  file=open(f"{folderName}/{fileName}","r")
  json_format=file.read()
  return json_format

def create_json_file(data,file_name):

  json_format=json.dumps(data,indent=4)
  file=open(f"json_embedding/{file_name}","w") # open the file in write mode 
  file.write(json_format) # we have wrote here 
  file.close()  # closed the file



count1=1
 # step-01 access all json files one by one thorugh the loop
for json_file in give_all_jason_files():
  if(count1==2):
     break

# read the json file content 
  json_content=read_json_file_content("json",json_file)

# parse the json content 
  parse_json=json.loads(json_content)


# now creating  a embeddings of each chunk  for  current file 
  segments=[]
  count2=1
  for chunk in parse_json["segements"]:
    if(count2==2):
       break
    text=chunk["text"]
    embedding=create_embedding(text)
    print(embedding)
    print(len(embedding))
    segments.append({ "lecture_id":chunk[ "lecture_id"],"lecture_title":chunk[" Install python on windows "],"start":chunk["start"],"end":chunk["end"],"text":chunk["text"],"embedding":embedding})
    count2=count2+1



  #create the json file with embdeeings 
  create_json_file(segments,json_file)
  count1=count1+1



    


  
   
