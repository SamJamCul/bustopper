import tflapi
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/main')
def main():
    return render_template('main.html')
