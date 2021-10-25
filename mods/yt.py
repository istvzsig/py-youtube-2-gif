# YOUTUBE VIDEO DOWNLOADER
from pytube import YouTube

# sadly pytube module does not support subclipping
# so we need to download the whole youtube video
# and cut it while processing gif

class YOUTUBE:
    @staticmethod
    def download(video_url:str) -> '.mp4':
        if not video_url: return # guardian

        # get first youtube video by url
        return (YouTube(video_url).streams
            .filter(progressive=True,
                    file_extension='mp4')
            .first() # get the best result
            .download(filename='downloaded.mp4',
                skip_existing=False)) # download video into root dir
    @staticmethod
    def converter(data:video):
        print(data.metadata)
        def cut():
            pass
