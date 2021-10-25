import asyncio
import json
# flask
from flask import Flask, render_template, request, redirect, url_for, jsonify, session

# mods dir
from mods.yt import YOUTUBE
from mods.gif import GIF
from mods.manager import File

# init flask app
app = Flask(__name__)

# https://www.youtube.com/watch?v=Tn6-PIqc4UM
# https://www.youtube.com/watch?v=kWsG2cIOvGk?start=22&end=25

def process_image(imageName):
    f = open(imageName+'.gif', 'rb')
    print(f)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        # start_time = request.form['start']
        duration = 3 # hard coded
        start_time = 22 # hard coded
        end_time = start_time + duration
        print('='*100)
        print('USER SENT URL:', url)
        print('='*100)
        try:
            yt = YOUTUBE.download(url) # download video
            # YOUTUBE.video(yt)
            print('Video from url', url, 'downloaded.')
            print('='*100)
            GIF.it() # create gif
            print('video converted')
            print('='*100)
        except Exception as e:
            print('='*100)
            print(e)
            print('='*100)

        print("Job's done.")
        # File.delete()
        return redirect(url_for('home'))
    # process_image('converted')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
