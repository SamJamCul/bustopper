import tflapi
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    bustuff = tflapi.makedat()
    route = bustuff[0][0]
    time = bustuff[0][1]
    return render_template('main.html', time=time, route=route)
