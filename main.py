import os

import function

'''
Only works if the movie is <= one hour. If the movie is longer than an hour, cut it into several 1-hour sections

'''

srt_file = "srtfile.srt"
folder_name = "Captain Philips"
movie_title = "movie.mp4"

os.mkdir(folder_name)

srt = open(f"{srt_file}", 'r', encoding="utf-8").read()
subtitle = function.parse_srt(srt)


for key in subtitle:
    title = key["content"]
    start = key["start"]
    end = key["end"]
    file_name = function.set_input_name(title)
    video = f"ffmpeg -y -ss {start} -to {end} -i {movie_title} -c copy {file_name}.mp4"
    os.system(video)
  

for files in os.listdir():
    if files.endswith(".mp4"):
        file_name = function.set_output_name(files)
        os.rename(files, f"{folder_name}/{file_name}.mp4")
    	
