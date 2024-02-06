from flask import Flask, Blueprint, request
from api.users.UserAPI import UserAPI
from api.auth.jwt_token import *
users = Blueprint('users', __name__)
userAPI = UserAPI()

@users.get('/')
@jwt_required()
def getUser():
    token = request.headers['Authorization']
    id = decode_jwt(token)
    userAPI.get_user(id)
    return f'{userAPI.user}'
