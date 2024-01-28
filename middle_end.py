import music_transcription
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('data')
    result = music_transcription.main(data)
    return jsonify(result='music.xml')


if __name__ == '__main__':
    app.run(debug=True)
