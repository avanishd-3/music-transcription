import music_transcription
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src/templates')


@app.route('/')
def hello():
    """
    Route decorator for the root URL that calls the hello function.
    Returns the rendered firstpage.html template.
    """
    return render_template('firstpage.html')


@app.route('/process', methods=['POST', 'GET'])
def process():
    """
    Function to handle the POST request to '/process' and return the rendered template.
    """
    data = request.form.get('url')
    result = music_transcription.main(data)

    return render_template('sheet_music_display.html')


if __name__ == '__main__':
    app.run(debug=True)
