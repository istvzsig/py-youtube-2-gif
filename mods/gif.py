from moviepy.editor import *

# FOR GIF
class GIF:
    @staticmethod
    def it() -> 'image':
        # size={'w': 400, 'h': 150}
        # object from video file
        clip = (VideoFileClip('downloaded.mp4')
            .subclip() # default 3 secs long gif
            .resize(1))

        # render the gif
        clip.write_gif('static/converted.gif')
