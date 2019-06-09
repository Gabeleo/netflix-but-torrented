import os
from flask import Flask, redirect, request, render_template
from forms import SearchForm
from htpc import Driver


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            input_text = request.form['text']
            return render_template('index.html')

    @app.route('/result')
    def result(input_text:
        dr = Driver('https://thepiratebay.org/')
        infohash = dr.__str__()
        return redirect(infohash, port=302)

    return app