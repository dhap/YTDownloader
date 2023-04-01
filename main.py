from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
import ffmpeg
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
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
print(yd, "Size - ", yd.filesize_mb, " Mb")

if yd.is_dash:
    print("need to download audio track for this choice")
    for a in yt.streams.filter(only_audio=any):
        print(a, "Size - ", a.filesize_mb, " Mb")

    itaga = int(input('Enter the itag number  '))
    yda = yt.streams.get_by_itag(itaga)
    needaudio = True

try:
    yd.download(".\\video")
except AttributeError as e:
    print("enter correct number of itag")

if needaudio:
    try:
        yda.download("\\audio")
    except AttributeError as e:
        print("enter correct number of itag")
    svideo = str(yd.download("\\video"))
    pathToSaveOutputVideo = svideo.replace("\\video","")
    saudio = str(yda.download("\\audio")) 

    # Open the video and audio
    video_clip = VideoFileClip(svideo)
    audio_clip = AudioFileClip(saudio)



    # Concatenate the video clip with the audio clip
    final_clip = video_clip.set_audio(audio_clip)

    # Export the final video with audio
    final_clip.write_videofile(title + ".mp4")


'''
    input_video = ffmpeg.input(svideo)
    input_audio = ffmpeg.input(saudio)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output(pathToSaveOutputVideo).run()
'''