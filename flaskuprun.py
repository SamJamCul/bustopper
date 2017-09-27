import tflapi
from flask import Flask
app = Flask(__name__)


@app.route('/')
def frontpage():
    intest = tflapi.makedat()
    if intest[0][1] <= 1:
        return 'A {} is arriving freakin\' soon!'.format(intest[0][0])
    else:
        return 'A {} is arriving in {} minutes!'.format(intest[0][0], intest[0][1])
