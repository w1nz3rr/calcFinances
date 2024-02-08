from flask import Flask
from api.api import api
from api.users.users import users
from api.auth.auth import auth
from api.categorys.categoryes import categoryes


from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'
jwt = JWTManager(app)

app.register_blueprint(api)
app.register_blueprint(users, url_prefix='/api/users')
app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(categoryes, url_prefix='/api/users/categoryes')


if __name__ == '__main__':
    app.run()
