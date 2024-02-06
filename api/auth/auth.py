from flask import Flask, Blueprint, request, jsonify
from api.auth.AuthAPI import AuthAPI
from api.auth.jwt_token import *

auth = Blueprint('auth', __name__)


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
    del user['password']
    return jsonify(user=user)


@auth.post('/login')
def login_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    Auth.login_by_password(login, password)

    if Auth.user == 'Нет такого пользователя':
        return jsonify(error="Неверный логин или пароль")

    user = Auth.user.__dict__
    del user['password']
    return jsonify(user=user)


