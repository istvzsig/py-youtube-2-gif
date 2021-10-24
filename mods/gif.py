from moviepy.editor import *

# FOR GIF
class GIF:
    @staticmethod
    def it(video_url:str=None) -> dict:
        if not video_url: return # guardian

        # object from video file
        clip = (VideoFileClip(video_url)
            .subclip((33),(36))
            .resize(.2))

        # render the gif
        clip.write_gif('converted.gif')
