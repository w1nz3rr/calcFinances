from flask import Flask
from api.api import api
from api.users.users import users
from api.auth.auth import auth
from api.categorys.category import category
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'SECRET_KEY'
jwt = JWTManager(app)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(users, url_prefix='/api/users')
app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(category, url_prefix='/api/users/categorys')

if __name__ == '__main__':
    app.run()
