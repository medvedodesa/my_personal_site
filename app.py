from flask import Flask
from flask import request
from flask import session
from flask import render_template, redirect, url_for, abort, g
from flask import send_from_directory
from flask_babel import Babel, get_locale

app = Flask(__name__)
# ...
babel = Babel(app)
LANGUAGES = ['en', 'ru']

@app.before_request
def before_request():
    g.locale = str(get_locale())


@babel.localeselector
def get_locale():

    return request.accept_languages.best_match(LANGUAGES)
#     return 'en'


@app.route('/', methods=['GET', 'POST'])
def index():

    a=g.locale
    return render_template('index.html', langs=LANGUAGES)

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory(filename, static_url_path='static')

if __name__ == '__main__':


    app.run()
