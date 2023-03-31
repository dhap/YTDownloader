from pytube import YouTube
from pytube.cli import on_progress
from sys import argv


try:
    url = argv[1]
except IndexError as e:
    print("Input the YouTube  video URL")
    url = str(input())

#if  len(argv) < 2:
#    print("Input the YouTube  video URL")
#    url = str(input())
#else:
#    url = str(argv)

yt = YouTube(url, on_progress_callback=on_progress)

print(yt.title)
print(yt.streams.filter(progressive=True))
yd = yt.streams.get_highest_resolution()

yd.download('c:\\Users\\draph\\YtDowloader\\')
input()