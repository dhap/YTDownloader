from pytube import YouTube
from pytube.cli import on_progress
import pytube.request
import requests
import ffmpeg


url = str()
itag = int()

pytube.request.default_range_size = 1048576 # 1Mb


def ffmegCombine(yd, yda, filename):


    input_video = ffmpeg.input(yd.download("Video"))
    input_audio = ffmpeg.input(yda.download("Audio"))
    ffmpeg.output(input_audio, input_video, filename, codec='copy').run()
   

def validateItag(streamsIn):
    while True:
        inputItag = str(input('Enter the itag number  '))
        for i in streamsIn:
            if "\"" + inputItag + "\"" in str(i):
                
                return i
        print("Enter correct number")


def main():
    yt = YouTube(validateUrl(), on_progress_callback=on_progress)
    title = str(yt.title)
    print(title)

    #Output streams
    for v in yt.streams.filter(type="video"):
        print(v, "    Size =", v.filesize_mb, "Mb")

    yd = validateItag(yt.streams.filter(type="video"))
    filename = yd.default_filename

    if "webm" in filename:
        mime_type = "webm"
    else: mime_type = "mp4"

    print("Selected stream - ", yd, "Size - ", yd.filesize_mb, "Mb")

    #Chek if it is only video stresm without audio line
    if yd.is_dash:
        print("need to download audio track for this choice")
        for a in yt.streams.filter(only_audio=True, file_extension=mime_type ):
            print(a, "Size - ", a.filesize_mb, "Mb")

        yda = validateItag(yt.streams.filter(only_audio=True, file_extension=mime_type))
        ffmegCombine(yd, yda, filename)

    else:
        yd.download()


#Validation URL
def validateUrl():  
    while True:
        print("Paste YouTube video url")
        url = input()
        if url.count("https://www.youtube.com") > 0:
            r = requests.get(url) 
            if 'unavailable_video.png' in r.text:
                print("This is not YouTube URL, input the YouTube video URL")
                continue
            else:
                return url
        else:
            print("This is not YouTube URL, input the YouTube video URL")
            continue


if __name__ == "__main__":
	main()