from flask import Flask
from api.api import api
from api.users.users import users
from api.auth.auth import auth
from api.categorys.categoryes import categoryes
from api.operations.operations import operations
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'
jwt = JWTManager(app)

app.register_blueprint(api)
app.register_blueprint(users)
app.register_blueprint(auth)
app.register_blueprint(categoryes)
app.register_blueprint(operations)


if __name__ == '__main__':
    app.run()
