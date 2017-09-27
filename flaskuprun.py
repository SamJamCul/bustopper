import tflapi
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/main')
def main():
    bustuff = tflapi.makedat()
    route = bustuff[0][0]
    time = bustuff[0][1]
    return render_template('main.html', time=time, route=route)
