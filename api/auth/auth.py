from flask import Flask, Blueprint
from api.auth.AuthAPI import AuthAPI

auth = Blueprint('auth', __name__)
Auth = AuthAPI()

@auth.post('/registration')
def register_user():
    login = request.json['login']
    password = request.json['password']
    auth.registration(login, password)

    return f'{auth.user}'