from pytube import YouTube
import os

#taking url input

yt = YouTube(str(input("Please enter the Url: \n>>")))

#extract audio data
video = yt.streams.filter(only_audio=True).first()

destination = "music"

out_file = video.download(output_path=destination)

#saving file

base, ext = os.path.splitext(out_file)
new_file = base + ".mp3"
os.rename(out_file, new_file)

print(yt.title + " Has been downloaded")