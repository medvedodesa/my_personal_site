from flask import Flask
from flask import request
from flask import render_template, g
from flask import send_from_directory
from flask_babel import Babel, get_locale, refresh


app = Flask(__name__)

babel = Babel(app)
LANGUAGES = ['en', 'ru']
lang=str(' ')


@app.before_request
def before_request():
    g.locale = str(get_locale())


@babel.localeselector
def get_locale():
    refresh()
    global lang
    if lang=='ru' or lang=='ru#':
        return 'ru'
    else:
        return 'en'



@app.route('/', methods=['GET', 'POST'])
def index():
    global lang
    lang=request.args.get('lang')
    g.locale = get_locale()
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory(filename, static_url_path='static')

if __name__ == '__main__':
    app.run()
