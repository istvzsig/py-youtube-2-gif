import asyncio
import json
from flask import Flask, render_template, request, redirect, url_for
from mods.yt import YOUTUBE
from mods.gif import GIF

app = Flask(__name__)
# https://www.youtube.com/watch?v=Tn6-PIqc4UM


def reponse_data():
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        print('='*100)
        print('video url:', url)
        print('='*100)
        try:
            YOUTUBE.download(url)
            print('='*100)
            print('Video from url', url, 'downloaded.')

            GIF.it('React in 100 Seconds.mp4')
            print('='*100)
            print('video converted')
            print('='*100)
        except Exception as e:
            print('='*100)
            print(e)
            print('='*100)

        print("Job's done.")
        return redirect(url_for('home'))
    return render_template('index.html', name=None)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
