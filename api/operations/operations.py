from flask import Flask, Blueprint, jsonify, request, abort
from api.operations.OperationsAPI import OperationsAPI
from api.operations.one_operationAPI import One_operationAPI
from api.auth.jwt_token import *

operations = Blueprint('operations', __name__, url_prefix='/api/users/categoryes/<category_id>/operations')
operationAPI = OperationsAPI()
one_operationAPI = One_operationAPI()


@operations.get('/')
@jwt_required()
def getOperations(category_id):
    token = request.headers['Authorization']
    id = decode_jwt(token)
    operationAPI.get_operation(id, category_id)
    return jsonify(operations=operationAPI.operations)

@operations.post('/')
@jwt_required()
def postOperations(category_id):
    token = request.headers['Authorization']
    type_operation = request.json['type_operation']
    value = request.json['value']
    description = request.json['description']

    id = decode_jwt(token)
    operationAPI.post_operation(type_operation, value, description, id, category_id)
    return jsonify(operations=operationAPI.operations)

@operations.get('/<id>')
@jwt_required()
def getOperation(category_id, id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)
    one_operationAPI.get_operation(user_id, id)
    if one_operationAPI.error == 'Нет операции':
        abort(404)
    return jsonify(operation=one_operationAPI.operation.__dict__)

@operations.delete('/<id>')
@jwt_required()
def deleteOperation(category_id, id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)
    if one_operationAPI.delete_operation(user_id, id):
        abort(204)
    else:
        return jsonify(status=False)

@operations.put('/<id>')
@jwt_required()
def putOperation(category_id, id):
    token = request.headers['Authorization']
    user_id = decode_jwt(token)

    type_operation = request.json['type_operation']
    value = request.json['value']
    description = request.json['description']

    one_operationAPI.put_operation(id, type_operation, value, description, user_id)
    return jsonify(operation=one_operationAPI.operation.__dict__)