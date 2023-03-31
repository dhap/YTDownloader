from pytube import YouTube
from pytube.cli import on_progress
from sys import argv


try:
    url = argv[1]
except IndexError as e:
    print("Input the YouTube  video URL")
    url = str(input())

yt = YouTube(url, on_progress_callback=on_progress)

print(yt.title)
for a in yt.streams:
    print(a)


itag = int(input('Enter the itag number  '))

yd = yt.streams.get_by_itag(itag)

yd.download()
