# we have to pull top matching chunks coressponding to the user query or question 
import requests
import os
import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

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



# step-01 query to vectors
input_query=input("enter your query:")

query_vector=create_embedding(input_query)[0]

# convert given query_vectors into the two dimnetinal 
query_vector_2d=[query_vector]


# collect the chunk_enbedding in 2 d 
chunks=[]
chunk_embeddings_2d=[]
for file in give_all_files("rawData/json_embedding")[:1]:
 content=read_file_content(f"rawData/json_embedding/{file}")

 original_content=json.loads(content)
 for chunk in original_content["segements"][:5]:
  chunks.append(chunk)
  chunk_embeddings_2d.append(chunk["embedding"])


# step-02 find the consine similarity 
similairty=cosine_similarity(query_vector_2d,chunk_embeddings_2d).flatten()

# finding a coresspopnding simlarity index in decsreasing order 
similairty_score_index = np.argsort(similairty)[::-1]

print("Similarity scores:",similairty)
print("similairty_score_index",similairty_score_index)

# step-03 pulling the top macthing chunk
top=5

top_matching_chunk_index=similairty_score_index[0:top:1]
print(top_matching_chunk_index)

top_matching_chunks = []

for index in top_matching_chunk_index:

    chunk = chunks[index]

    top_matching_chunks.append({
        "lecture_id": chunk["lecture_id"],
        "lecture_title": chunk["lecture_title"],
        "start": chunk["start"],
        "end": chunk["end"],
        "text": chunk["text"]
    })

print(top_matching_chunks)
