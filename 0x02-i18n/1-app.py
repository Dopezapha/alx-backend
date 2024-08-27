#!/usr/bin/env python3
"""
Basic Babel Setup
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class config:
    """
    Configuration class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(config)


@app.route('/')
def index():
    """
    Defines a function called index
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
