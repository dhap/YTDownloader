from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
import ffmpeg
import os



needaudio = False
itag = int()

try:
    url = argv[1]
except IndexError as e:
    print("Input the YouTube video URL")
    url = str(input())

yt = YouTube(url, on_progress_callback=on_progress)

title = str(yt.title)
title = title.replace("//",'')
print(title)

for a in yt.streams:
    print(a, "Size in Mb ", a.filesize_mb)

itag = int(input('Enter the itag number  '))


yd = yt.streams.get_by_itag(itag)
print(yd, "Size in Mb ", yd.filesize_mb)

if yd.is_dash:
    print("need audio track")
    for a in yt.streams.filter(only_audio=any):
        print(a, "Size in Mb ", a.filesize_mb)

    itaga = int(input('Enter the itag number  '))
    yda = yt.streams.get_by_itag(itaga)
    needaudio = True

try:
    yd.download()
except AttributeError as e:
    print("enter correct number of itag")

if needaudio:
    
    try:
        yda.download(".\\audio")    
    except AttributeError as e:
        print("enter correct number of itag")

    input_video = ffmpeg.input(yd.download())
   
    input_audio = ffmpeg.input(yda.download(".\\audio"))
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('1.mp4').run()
