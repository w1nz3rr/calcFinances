from flask import Flask, Blueprint, request, jsonify, abort
from api.auth.AuthAPI import AuthAPI
from api.auth.jwt_token import *

auth = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth.post('/registration')
def register_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    confirm_password = request.json['confirm_password']

    if password != confirm_password:
        return jsonify(error="Пароли не совпадают")
    Auth.registration(login, password)

    if Auth.user == "Данный логин занят":
        return jsonify(error="Данный логин занят")

    user = Auth.user.__dict__
    token = create_token({'id': user['id']})
    del user['password']
    return jsonify(user=user, token=token)


@auth.post('/login')
def login_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    Auth.login(login, password)

    if Auth.user == 'Нет такого пользователя':
        abort(401)
        # return jsonify(error="Неверный логин или пароль")

    user = Auth.user.__dict__
    token = create_token({'id': user['id']})
    del user['password']
    return jsonify(user=user, token=token)
