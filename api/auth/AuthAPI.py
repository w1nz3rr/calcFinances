from api.DB.db import *
from api.DB.db_class import *
from api.users.UserAPI import UserAPI

class AuthAPI(UserAPI, DB):
    user = User

    def take_user(self, login):
        query = 'select * from users where login = ?'
        self.execute_query(query, login, is_select=True)

    def registration(self, login, password):
        self.take_user(login)
        if self.cache:
            self.user = 'данный логин занят'
            return False
        query = 'insert into users (login, password) values (?, ?)'
        self.execute_query(query, login, password, is_select=False)
        self.take_user(login)
        self.set_user()

    def login_by_password(self, login, password):
        query = 'select * from users where login = ? and password = ?'
        self.execute_query(query, login, password, is_select=True)
        self.set_user()


