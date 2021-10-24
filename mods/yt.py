# YOUTUBE VIDEO DOWNLOADER
from pytube import YouTube

class YOUTUBE:
    @staticmethod
    def download(video_url:str) -> '.mp4':
        if not video_url: return # guardian

        # get first youtube video by url
        return (YouTube(video_url).streams
            .filter(progressive=True,
                    file_extension='mp4')
            .first() # get the best result
            .download(filename='downloaded.mp4')) # download video into root dir
    @staticmethod
    def set_name():
        pass
