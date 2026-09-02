# objective:converting audio file to text

import whisper  # external module 

import os      # internal module 

import json    # external module 

# now using whisper we have to convert our audio file into the text

# step-01 load the whisper model 
model=whisper.load_model("base")


files=os.listdir("audio")  # array of files 


# excess each file and transcibe it 

for file in files:

  lecture_num=file.split("_")[0]
  lecture_title=file.split("_")[1].split(".")[0]

  # Step 02: Transcribe the audio file

  print(f"prcoessing the : {file}")
  text_result=model.transcribe(
    f"audio/{file}",
    task="transcibe",
    language="en"
  )

  print(text_result)  # dicstinalry 
  print(type(text_result)) # dictinalry 

  # extract usefull information 
  segements=[]


  for chunk  in text_result["segments"]:
    segements.append({"lecture_id":chunk["id"],"lecture_title":lecture_title,"start":chunk["start"],"end":chunk["end"],"text":chunk["text"]})



  json_format=json.dumps({"text":text_result["text"],"segements":segements}, indent=4) # it will convert the python data type in to json 
  print(type(json_format))


  # now bcz we have a json data now we can save it in a file 
  file_name=f"{lecture_num}_{lecture_title}"
  file=open(f"rawData/json/{file_name}.json","w") #open the file in write mode 
  file.write(json_format) # we have wrote here 
  file.close()  # closed the file



# problem here is we have transcribe only one file but we should do it for all audio file 
