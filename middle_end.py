import music_transcription
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='src/templates')


@app.route('/')
def hello():
    return render_template('firstpage.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.form.get('url')
    result = music_transcription.main(data)
    # return jsonify(result='music.xml')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
