from flask import Flask, Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)
jwt = JWTManager(app)
cors = CORS(app)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'
app.config['CORS_HEADERS'] = 'Content-Type'

auth = Blueprint('auth', __name__, url_prefix='/api/auth')
app.register_blueprint(auth)

users = Blueprint('users', __name__, url_prefix='/api/users')
app.register_blueprint(users)

categoryes = Blueprint('category', __name__, url_prefix='/api/users/categoryes')
app.register_blueprint(categoryes)

operations = Blueprint('operations', __name__, url_prefix='/api/users/categoryes/<category_id>/operations')
app.register_blueprint(operations)



if __name__ == '__main__':
    app.run()
