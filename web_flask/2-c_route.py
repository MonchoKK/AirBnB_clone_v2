#!/usr/bin/python3
"""Starts a Flask web application:
- The web application must be listening on 0.0.0.0, port 5000
- Routes:
  - /: display "Hello HBNB!"
  - /hbnb: display "HBNB"
  - /c/<text>: display "C " followed by the value of the text variable
    (replace underscore _ symbols with spaces)
- You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)
app.url_map.strict_slashes = False  # Override default globally


@app.route('/')
def hello_hbnb():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Returns 'C ' followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
