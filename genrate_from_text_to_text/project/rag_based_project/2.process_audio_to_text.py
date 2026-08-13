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

file=os.open("json/1.first.json","w")
json_result=json.loads(text_result)
file.write(json_result)
file.close()

print(text_result)