from flask import Flask, Blueprint, jsonify, request, abort
from api.categorys.CategoryesAPI import CategoryesAPI
from api.categorys.one_categoryAPI import One_categoryAPI
from api.auth.jwt_token import *

categoryes = Blueprint('category', __name__, url_prefix='/api/users/categoryes')
categoryAPI = CategoryesAPI()
one_categoryAPI = One_categoryAPI()


@categoryes.get('/')
@jwt_required()
def getCategoryes():
    token = request.headers['Authorization']
    id = decode_jwt(token)
    categoryAPI.get_category(id)
    return jsonify(categorys=categoryAPI.categoryes)


@categoryes.post('/')
@jwt_required()
def postCategory():
    token = request.headers['Authorization']
    name = request.json['name']
    description = request.json['description']

    id = decode_jwt(token)
    categoryAPI.post_category(name, description, id)
    return jsonify(categorys=categoryAPI.categoryes)




@categoryes.get('/<id>')
@jwt_required()
def getCategory(id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)
    one_categoryAPI.get_category(user_id, id)
    if one_categoryAPI.error == 'Нет категории':
        abort(404)
    return jsonify(category=one_categoryAPI.category.__dict__)


@categoryes.delete('/<id>')
@jwt_required()
def deleteCategory(id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)
    if one_categoryAPI.delete_category(user_id, id):
        abort(204)
    else:
        return jsonify(status=False)


@categoryes.put('/<id>')
@jwt_required()
def putCategory(id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)

    name = request.json['name']
    description = request.json['description']
    color = request.json['color']

    one_categoryAPI.put_category(id, user_id, name, description, color)
    return jsonify(category=one_categoryAPI.category.__dict__)