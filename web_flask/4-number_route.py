#!/usr/bin/python3
"""script that starts a Flask web application, display “Hello HBNB!”"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hellobnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    display_text = text.replace('_', ' ')
    return 'Python {}'.format(display_text)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
