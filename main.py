from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import requests

needaudio = False
url = str()
itag = int()

#Check argument
try:
    url = argv[1]
except IndexError as e:
    print("No have argument")

#Validation URL
while True:
    if url == "":
        print("Input the YouTube video URL")
        url = str(input())
    if url.count("https://www.youtube.com") > 0:
        r = requests.get(url) # random video id
        if 'unavailable_video.png' in r.text:
            print("Video unavailable")
            print("Input the YouTube video URL")
            url = str(input())
            continue
        else:
            yt = YouTube(url, on_progress_callback=on_progress)
            break
    else:
        print("This is not YouTube URL")
        print("Input the YouTube video URL")
        url = str(input())
        continue

title = str(yt.title)
title = title.replace("//",'')
print(title)

for a in yt.streams.filter(mime_type="video/mp4"):
    print(a, "Size - ", a.filesize_mb, "Mb")

itag = int(input('Enter the itag number  '))

#Select id video stream
yd = yt.streams.get_by_itag(itag)
print("Selected stream - ", yd, "Size - ", yd.filesize_mb, "Mb")

#Chek if it is only video stresm without audio line
if yd.is_dash:
    print("need to download audio track for this choice")
    for a in yt.streams.filter(only_audio=any):
        print(a, "Size - ", a.filesize_mb, "Mb")

    itaga = int(input('Enter the itag number  '))
    yda = yt.streams.get_by_itag(itaga)
    needaudio = True

try:
    yd.download()
except AttributeError as e:
    print("Enter correct number of itag")

if needaudio:
    try:
        yda.download("\\YTD_audio")
    except AttributeError as e:
        print("enter correct number of itag")
    svideo = str(yd.download("\\YTD_video"))
    pathToSaveOutputVideo = svideo.replace("\\YTD_video","")
    saudio = str(yda.download("\\YTD_audio")) 

    # Open the video and audio
    video_clip = VideoFileClip(svideo)
    audio_clip = AudioFileClip(saudio)

    # Concatenate the video clip with the audio clip
    final_clip = video_clip.set_audio(audio_clip)

    # Export the final video with audio
    final_clip.write_videofile(title + ".mp4")