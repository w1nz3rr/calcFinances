from flask import Flask
from apiClass import *

app = Flask(__name__)


@app.get('/api/users/<id>')
def get_user(id):
    userApi = UserApi()
    userApi.get_user(id)

    return f'{userApi.user}'


if __name__ == '__main__':
    app.run()
