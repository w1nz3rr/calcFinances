from flask_jwt_extended import create_access_token, decode_token


def create_token(data):
    token = create_access_token(identity=data)
    return token

def decode_token(token):
    data = decode_token(token)
    return data
