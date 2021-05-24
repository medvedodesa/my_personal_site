from flask import Flask
from flask import request
from flask import session
from flask import render_template, redirect, url_for
from flask import send_from_directory
from flask_babel import Babel

app = Flask(__name__)
# ...
babel = Babel(app)
LANGUAGES = ['en', 'ru']

@babel.localeselector
def get_locale():


    return request.accept_languages.best_match(LANGUAGES)
#     return 'en'

# @app.context_processor
# def inject_conf_var():
#     return dict(
#                 AVAILABLE_LANGUAGES=LANGUAGES,
#                 CURRENT_LANGUAGE=session.get('language',request.accept_languages.best_match(LANGUAGES)))






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def send_js(filename):
    return send_from_directory(filename, static_url_path='static')

if __name__ == '__main__':
    app.run()
