import flask
from flask import Flask
app = Flask(__name__)

@app.route('/code/inject.js')
def get_code():
    return flask.url_for("static", "inject.js")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
