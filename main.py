from pytube import YouTube
from pytube.cli import on_progress

yt = YouTube('https://www.youtube.com/watch?v=xbNzZMfDF-8',on_progress_callback=on_progress)

print(yt.title)
print(yt.streams)
yd = yt.streams.get_highest_resolution()

yd.download('c:\\Users\\draph\\YtDowloader\\')