from flask import Flask, request
from apiClass import *

app = Flask(__name__)
userAPI = UserAPI()

@app.get('/api/users/<id>')
def get_user(id):
    userAPI.get_user(id)
    return f'{userAPI.user}'


@app.post('/api/users')
def post_user():
    login = request.json['login']
    password = request.json['password']
    userAPI.post_user(login, password)

    return f'{userAPI.user}'



if __name__ == '__main__':
    app.run()
