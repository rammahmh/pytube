from pytube import YouTube
from pytube.cli import on_progress
import ffmpeg

# assign the link of YouTube video to the YouTube object
print("Enter YouTube Link: ")
videoLink = input()
yt = YouTube(videoLink, on_progress_callback=on_progress)

# useful variables
ytTitle = yt.title
print(ytTitle)

# video/ audio quality based on itag, further read https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f
# TODO: make getting the highest resolution dynamic
video_stream = yt.streams.first()
audio_stream = yt.streams.first()

# indicator for easy interpreting
print("Download started..")

# variable title of the video to change the name of the video later
rename_video = str(ytTitle)
rename_video1 = rename_video+" video"

# variable title of the video to change the name of the video later
rename_audio = str(ytTitle)
rename_audio1 = rename_audio+" audio"

# download the video and store it into ~/Downloads and rename the filename.
print("Video download started..")
video_stream.download('~/Downloads', filename=rename_video1)
print(video_stream, "done downloading video")

# download the video and store it into ~/Downloads and rename the filename.
print("Audio download started..")
audio_stream.download('~/Downloads', filename=rename_audio1)
print(audio_stream, "done downloading audio")

# Variables to contain the file names of video and audio going to be merged.
video_input = ffmpeg.input(f"~/Downloads/{ytTitle} video")
audio_input = ffmpeg.input(f"~/Downloads/{ytTitle} audio")

# Used to concat the video and audio together and output the new file.
# TODO: variable for the output filename
ffmpeg.concat(video_input, audio_input, v=1, a=1).output(f"~/Downloads/{ytTitle} completed").run()


print("Done")
