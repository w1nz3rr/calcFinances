from flask import Flask, Blueprint
from api.users.UserAPI import UserAPI
users = Blueprint('users', __name__)
userAPI = UserAPI()

@users.get('/<id>')
def getUser(id):
    userAPI.get_user(id)
    return f'{userAPI.user}'
