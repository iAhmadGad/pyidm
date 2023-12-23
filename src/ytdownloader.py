from pytube import YouTube

def download(url):
    YouTube(url).streams.first().download()
    yt = YouTube(url)
    yt.streams
    .filter(progressive = True, file_extension = "mp4")
    .order_by("resolution")
    .desc()
    .first()
    .download()
