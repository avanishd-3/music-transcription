import pytube


def youtube_link_to_mp3(link: str) -> None:
    """ Convert Youtube link to mp3 file"""
    yt_obj = pytube.YouTube(link)

    audio = yt_obj.streams.filter(only_audio=True).first().download(filename="audio.mp3")




youtube_link_to_mp3("https://youtu.be/SWKR0BzL_z0")
