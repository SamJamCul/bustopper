import tflapi
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    intest = tflapi.makedat()
    return intest[1]
