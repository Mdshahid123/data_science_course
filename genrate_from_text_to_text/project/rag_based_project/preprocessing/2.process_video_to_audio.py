# previuosly we saved the audio file with same name as of video file 
# that file name contain many thing 
# so will be  use onlu lecture number and lecture tile as a file name 

import subprocess
import os 


# input video file ino the audio output file

files=os.listdir("rawData/videos")  # it will return the list of files 


for file in files:

  lecture_num=file.split("_")[0]
  lecture_title=file.split("_")[1].split("[")[0]


  input_video_path=f"rawData/videos/{file}"

  output_audio_path=f"raw/audio/{lecture_num}_{lecture_title}.mp3"

  subprocess.run(["ffmpeg","-i",input_video_path,output_audio_path])