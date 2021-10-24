from pytube import YouTube
from moviepy.editor import *

# OBJECT FOR YOUTUBE VIDEO
class YOUTUBE:
    @staticmethod
    def download(video_url=None):
        if not video_url: return # guardian

        # get first youtube video by url
        return (YouTube(video_url).streams
            .filter(progressive=True,
                    file_extension='mp4')
            .first() # get the best result
            .download()) # download video to root dir
    @staticmethod
    def rename():
        pass

# OBJECT FOR CREATE GIFS
class GIF:
    @staticmethod
    def it(video_url=None) -> []:
        if not video_url: return # guardian
        # object from video file
        clip = (VideoFileClip(video_url)
            .subclip((33),(36))
            .resize(.2))

        # render the gif
        clip.write_gif('converted.gif')
