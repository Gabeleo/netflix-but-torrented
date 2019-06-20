import os
from flask import Flask, redirect, request, render_template
from flaskr.depend.htpc import Driver



def create_app(test_config=None):
    """Creates and configures the Flask application."""
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

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/result', methods=['GET', 'POST'])
    def result():
        if request.method == 'POST':
            query = request.form['text']
            htpc.create("https://thepiratebay.org/", query)
            return redirect(htpc.infohash)

    return app