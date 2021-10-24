from pytube import YouTube
from moviepy.editor import *
# import asyncio
# import websockets

# async def hello():
#     async with websockets.connect("ws://localhost:8765") as websocket:
#         await websocket.send("Hello world!")
#         await websocket.recv()

# asyncio.run(hello())

class YOUTUBE(object):
    @staticmethod
    def download(video_url=None):
        if not video_url: return
        return (YouTube(video_url).streams
            .filter(progressive=True,
                    file_extension='mp4')
            .first()
            .download())
    @staticmethod
    def rename():
        pass

class GIF(object):
    @staticmethod
    def it(video_url=None):
        if not video_url: return
        clip = (VideoFileClip(video_url)
            .subclip((33),(36))
            .resize(.2))

        clip.write_gif('converted.gif')

if __name__ == '__main__':
    try:
        pass
        # (YOUTUBE.download('https://youtu.be/ACp0zmWJXBg'),
        # GIF.it('NEW SIZE! Shadow Rap Jack Deep 07 I Rapala®.mp4')
    except Exception as e:
        print(e)