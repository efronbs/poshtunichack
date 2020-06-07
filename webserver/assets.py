import flask
from flask import Flask
app = Flask(__name__)

@app.route('/html')
def get_html():
    return app.send_static_file("inject.html")

@app.route('/js')
def get_js():
    return app.send_static_file("inject.js")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
