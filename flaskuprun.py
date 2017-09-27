import tflapi
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buses')
def buses():
    bustuff = tflapi.makedat()
    route = bustuff[0][0]
    time = bustuff[0][1]
    return render_template('buses.html', time=time, route=route)

@app.route('/weather')
def weather():
    return render_template('weather.html')
