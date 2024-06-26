#!/usr/bin/python3
"""script that starts a Flask web application, display “Hello HBNB!”"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hellobnb():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
