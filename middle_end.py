import music_transcription
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='src/templates')


@app.route('/')
def hello():
    """
    Route decorator for the root URL that calls the hello function.
    Returns the rendered firstpage.html template.
    """
    return render_template('firstpage.html')


@app.route('/process', methods=['POST'])
def process():
    """
    Function to handle the POST request to '/process' and return the rendered template.
    """
    data = request.form.get('url')
    result = music_transcription.main(data)
    # return jsonify(result='music.xml')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
