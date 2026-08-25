import os
import json
import requests



def give_all_files(dirName):
 json_files=os.listdir(dirName)
 #print(json_files) # it will give all the files name in list
 return json_files

def read_file_content(file_path):
 #lets read the content of current json file
 read_file=open(file_path,"r")
 content=read_file.read()
 read_file.close()
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
 return actual_response["embeddings"]

def store_as_json(data,path):
 file=open(path,"w")
 json_format=json.dumps(data,indent=4)
 file.write(json_format)
 file.close()
 
 

for json_file in give_all_files("json"):
 
  print("current_file:",json_file)
  
   
# step 1=reading a content of current file
  content=read_file_content(f"json/{json_file}")

  #step2= parse the current json file
  parsed_content=json.loads(content)
  
  all_text=[]
  #collecting all text
  for chunk in parsed_content["segements"]:
    all_text.append(chunk["text"])

  print(f"processing_the:{json_file}")
  embedding_vectors=create_embedding(all_text)

  # now store the embeddings in json file 
  segments=[]
  for chunk, embedding_vector in zip(
        parsed_content["segements"],
        embedding_vectors
    ):
    chunk["embedding"]=embedding_vector
    segments.append(chunk)
   


  store_as_json({"text":parsed_content["text"],"segements":segments},f"json_embedding/{json_file}")
  

  
  

  

  




  
  
