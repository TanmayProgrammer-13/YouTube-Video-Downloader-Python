from pytube import YouTube

Link= "https://www.youtube.com/watch?v=PicLAm0AWvE"

video= YouTube(Link)

stream= video.stream.get_highest_resolution()

stream.download()