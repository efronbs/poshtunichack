import flask
from flask import Flask
app = Flask(__name__)

@app.route('/html')
def get_code():
    return app.send_static_filename("inject.html")

@app.route('/js')
def get_code():
    return app.send_static_filename("inject.js")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
