import music_transcription
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src/templates')


@app.route('/')
def hello():
    return render_template('firstpage.html')


@app.route('/process', methods=['POST', 'GET'])
def process():
    data = request.form.get('url')
    result = music_transcription.main(data)

    return render_template('sheet_music_display.html')


if __name__ == '__main__':
    app.run(debug=True)
