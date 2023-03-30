from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=xbNzZMfDF-8')

print(yt.title)
print(yt.streams)
yd = yt.streams.get_highest_resolution()

yd.download('c:\\Users\\draph\\YtDowloader\\')