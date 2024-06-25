from flask import Flask
from main import scrape
from pandasWork import costAssembly

app = Flask(__name__)

@app.route('/')
def index():
    return('<p>Flask started successfully</p>')

@app.route('/test')
def test():
    count = 0
    count += 1
    return('<p> count is' + str(count) + '</p>')

# @app.route('/scrape')
# def doScrape():
#     scrape()

# @app.route('/assemble')
# def doAssemble():
#     costAssembly()