from flask import Flask, Blueprint, request
from api.auth.AuthAPI import AuthAPI

auth = Blueprint('auth', __name__)
Auth = AuthAPI()

@auth.post('/registration')
def register_user():
    login = request.form['login']
    password = request.form['password']
    Auth.registration(login, password)

    return f'{Auth.user}'


@auth.post('/login')
def login_user():
    login = request.form['login']
    password = request.form['password']
    Auth.login_by_password(login, password)

    return f'{Auth.user}'


