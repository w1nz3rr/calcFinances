from flask import Flask, Blueprint, request, jsonify
from api.auth.AuthAPI import AuthAPI
from api.auth.jwt_token import *

auth = Blueprint('auth', __name__)


@auth.post('/registration')
def register_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    nickname = request.json['nickname']
    confirm_password = request.json['confirm_password']

    if password != confirm_password:
        return jsonify(error="Пароли не совпадают")
    Auth.registration(login, password, nickname)

    if Auth.user == "Данный логин занят":
        return jsonify(error="Данный логин занят")
    print(Auth.user)
    user = Auth.user.__dict__
    token = create_token({'id':user['id']})
    del user['password']
    return jsonify(user=user, token=token)


@auth.post('/login')
def login_user():
    Auth = AuthAPI()
    login = request.json['login']
    password = request.json['password']
    Auth.login_by_password(login, password)

    if Auth.user == 'Нет такого пользователя':
        return jsonify(error="Неверный логин или пароль")

    user = Auth.user.__dict__
    token = create_token({'id': user['id']})
    del user['password']
    return jsonify(user=user, token=token)

@auth.post('/decode')
@jwt_required()
def jwttoken():
    token = request.headers['Authorization']
    decode = decode_jwt(token)
    return jsonify(token=token, decode=decode)


