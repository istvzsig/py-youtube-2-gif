import asyncio
from flask import Flask, render_template, request, redirect, url_for
from main import YOUTUBE, GIF

app = Flask(__name__)
# https://www.youtube.com/watch?v=Tn6-PIqc4UM

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        print('video url:', url)
        try:
            YOUTUBE.download(url)
            print('video downloaded')
            GIF.it('React in 100 Seconds.mp4')
            print('video converted')
        except Exception as e:
            print(e)

        print('video downloaded')
        return redirect(url_for('home'))
    return render_template('index.html', name="asdsd")

if __name__ == '__main__':
    app.run(debug=True, port=5555)