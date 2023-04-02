from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import requests
import ffmpeg

url = str()
itag = int()

#If stream without audio line
def needaudiosplit(yd, yda):
    svideo = str(yd.download(".TYD"))
    saudio = str(yda.download(".TDA")) 
    print(svideo,"================", saudio)
    # Open the video and audio
    video_clip = VideoFileClip(svideo)
    audio_clip = AudioFileClip(saudio)

    # Concatenate the video clip with the audio clip
    final_clip = video_clip.set_audio(audio_clip)
    SvideoOutput = svideo.replace(".mp4", "")
    SvideoOutput = SvideoOutput.replace(".TYD","")
    # Export the final video with audio
    final_clip.write_videofile(svideo + ".mp4")

def validateItag(streamsIn):
    while True:
        inputItag = str(input('Enter the itag number  '))
        for a in streamsIn:
            if "\"" + inputItag + "\"" in str(a):
                print(a)
                return a
        print("Enter correct number")


def ffmegCombine(yd, yda):

    input_video = ffmpeg.input(yd.download(".TYD"))
    print(input_video)
    input_audio = ffmpeg.input(yda.download(".TDA"))
    print(input_audio)
    ffmpeg.concat(input_video, input_audio, v=1, a=1).output('ffmpeg.mp4').run()

        
#Check argument
def main():
    yt = YouTube(validateUrl(), on_progress_callback=on_progress)
    title = str(yt.title)
    print(title)

    #Output streams
    for a in yt.streams.filter(mime_type="video/mp4"):
        print(a, "    Size =", a.filesize_mb, "Mb")

    yd = validateItag(yt.streams.filter(mime_type="video/mp4"))

    print("Selected stream - ", yd, "Size - ", yd.filesize_mb, "Mb")

    #Chek if it is only video stresm without audio line
    if yd.is_dash:
        print("need to download audio track for this choice")
        for a in yt.streams.filter(only_audio=any):
            print(a, "Size - ", a.filesize_mb, "Mb")

        yda = validateItag(yt.streams.filter(only_audio=any))
        choise = int(input("Input 1, to choise pymovie, or 2 to choise ffmpeg"))

        if choise == 1:
            needaudiosplit(yd, yda)
        if choise == 2:
            ffmegCombine(yd, yda)
    
    else:
        try:
            yd.download()
        except AttributeError as e:
            print("Enter correct number of itag")



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