import os
import json
import requests

def give_all_files():
 json_files=os.listdir("json")
 #print(json_files) # it will give all the files name in list
 return json_files

def read_file_content(file_path):
 #lets read the content of current json file
 read_file=open(file_path,"r")
 content=read_file.read()
 return content


def create_embedding(text):
 api_endpoint="http://localhost:11434/api/embed"

 payload={
  "model":"bge-m3",
  "input":text
 }

 headers={"content-type":"application/json"}

 response=requests.post(api_endpoint,json=payload,headers=headers)
 print(response)
 actual_response=response.json()
 return actual_response["embeddings"][0]

 

 


 

for json_file in give_all_files():
  
  
# step 1=reading a content of current file
  content=read_file_content(f"json/{json_file}")
  #step2= parse the current json file
  parsed_content=json.loads(content)
  
  segments=[]
  #now we have to create a embedding
  
  for chunk in parsed_content["segements"]:
  
   
    embedding_vector=create_embedding(chunk["text"])
    segments.append({
    "lecture_id":chunk["lecture_id"],
    "lecture_title":chunk["lecture_title"],
    "start":chunk["start"],
    "end":chunk["end"],
    "text":chunk["text"],
    "embedding_vector":embedding_vector
    })
    #now we have to save this embedding vector in json file for future processing 
    file=open(f"json_embedding/{json_file}","w")
    json_format=json.dumps({"text":parsed_content["text"],"segments":segments},indent=4)

    file.write(json_format)
    
    
  

  
  

  

  




  
  
