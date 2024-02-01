from flask import Flask, request
from apiClass import *

app = Flask(__name__)


@app.get('/api/users/<id>')
def get_user(id):
    userApi = UserApi()
    userApi.get_user(id)

    return f'{userApi.user}'


@app.post('/api/users')
def post_user():
    userApi = UserApi()
    login = request.json['login']
    password = request.json['password']
    userApi.post_user(login, password)

    return f'{userApi.user}'

if __name__ == '__main__':
    app.run()
