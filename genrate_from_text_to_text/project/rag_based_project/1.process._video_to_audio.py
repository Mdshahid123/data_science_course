import subprocess   #internal module 
import os           # internal module 


# input video file ino the audio output file

files=os.listdir("videos")  # it will return the list of files 


for file in files:

  print(f"processing a {file} ")

  video_path=f"videos/{file}"

  audio_file_name=file.split(".")[0]

  audio_path=f"audio/{audio_file_name}.mp3"

  subprocess.run(["ffmpeg","-i",video_path,audio_path])



