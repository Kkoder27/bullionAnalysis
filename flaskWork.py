from flask import Flask

app = Flask(__name__)

@app.route('/')
def testFunct():
    return('<p>Flask Test performed successfully</p>')