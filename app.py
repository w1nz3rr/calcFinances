from flask import Flask
from apiClass import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world'


if __name__ == '__main__':
    app.run()
