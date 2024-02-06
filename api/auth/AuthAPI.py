from api.DB.db import *
from api.DB.db_class import *
from api.users.UserAPI import UserAPI

class AuthAPI(UserAPI, DB):
    user = User

    def registration(self, login, password):
        query = 'insert into users (login, password) values (?, ?)'
        self.execute_query(query, login, password, is_select=False)
        query = 'select * from users where login = ?'
        self.execute_query(query, login, is_select=True)
        self.set_user()

    def login_by_password(self, login, password):
        query = 'select * from users where login = ? and password = ?'
        self.execute_query(query, login, password, is_select=True)
        self.set_user()

    def login_by_id(self, id):
        query = 'select * from users where id = ?'
        self.execute_query(query, id, is_select=True)
        self.set_user()