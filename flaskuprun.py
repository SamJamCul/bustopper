import tflapi
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    intest = tflapi.makedat()
    return 'A {} is arriving in {} minutes'.format(intest[0][0], intest[0][1])
