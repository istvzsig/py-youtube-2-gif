from moviepy.editor import *

# FOR GIF
class GIF:
    @staticmethod
    def it() -> 'image':
        # object from video file
        clip = (VideoFileClip('downloaded.mp4')
            .subclip((81),(84))
            .resize(.7))

        # render the gif
        clip.write_gif('static/converted.gif')
