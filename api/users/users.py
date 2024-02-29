from flask import Blueprint, request, jsonify, abort

from api.auth.jwt_token import *
from api.users.UserAPI import UserAPI

users = Blueprint('users', __name__, url_prefix='/api/users')
userAPI = UserAPI()


@users.get('/')
@jwt_required()
def getUser():
    token = request.headers['Authorization']
    id = decode_jwt(token)
    userAPI.get_user(id)
    user = userAPI.user.__dict__
    del user['password']
    return jsonify(user=user)


@users.delete('/')
@jwt_required()
def deleteUser():
    token = request.headers['Authorization']
    id = decode_jwt(token)
    if userAPI.delete_user(id):
        abort(204)
    else:
        return jsonify(status=False)


@users.put('/')
@jwt_required()
def putUser():
    token = request.headers['Authorization']
    nickname = request.json['nickname']
    id = decode_jwt(token)
    userAPI.put_user(id, nickname)
    if userAPI.error == 'Ошибка изменения':
        return jsonify(error='Ошибка изменения')
    user = userAPI.user.__dict__
    del user['password']
    return jsonify(user=user)
