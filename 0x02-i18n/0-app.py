#!/usr/bin/env python3
"""
A Basic App
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Defines a function called index
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
