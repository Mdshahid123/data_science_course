import whisper  # external module 

import os 

import json
# now using whisper we have to convert our audio file into the text


# step-01 load the whisper model 
model=whisper.load_model("base")

# Step 02: Transcribe the audio file
text_result=model.transcribe(
  "audio/1_ Install python on windows [Python 3 Programming Tutorials] (1).mp3",
  task="translate",
  language="hi"
)

print(text_result)  # dicstinalry 
print(type(text_result)) # dictinalry 

# extract usefull information 

segements=[]


for chunk  in text_result["segments"]:
  segements.append({"id":chunk["id"],"start":chunk["start"],"end":chunk["end"],"text":chunk["text"]})



json_format=json.dumps({"text":text_result["text"],"segements":segements}, indent=4) # it will convert the python data type in to json 
print(type(json_format))


# now bcz we have a json data now we can save it in a file 
file=open("json/1.first.json","w") #open the file in write mode 
file.write(json_format) # we have wrote here 
file.close()  # clsed the file

