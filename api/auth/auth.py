from flask import Flask, Blueprint, request
from api.auth.AuthAPI import AuthAPI

auth = Blueprint('auth', __name__)


@auth.post('/registration')
def register_user():
    Auth = AuthAPI()
    login = request.form['login']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if password != confirm_password:
        return 'Пароли не совпадают'
    Auth.registration(login, password)

    return f'{Auth.user}'


@auth.post('/login')
def login_user():
    Auth = AuthAPI()
    login = request.form['login']
    password = request.form['password']
    Auth.login_by_password(login, password)
    if Auth.user == 'Нет такого пользователя':
        return 'Неверный логин или пароль'

    return f'{Auth.user}'


