from db import *
from db_class import *


class UserApi(User, DB):
    user: User


    def __init__(self):
        super().__init__()
        self.user = User()

    def set_user(self):
        if self.cache:
            self.user.id, self.user.login, self.user.password, self.user.create_at, self.user.update_at = self.cache
        else:
            self.user = f'Нет такого пользователя'


    def get_user(self, id):
        query = 'select * from users where id = ?'
        self.execute_query(query, id, is_select=True, is_one=True)
        self.set_user()


    def post_user(self, login, password):
        query = f'insert into users (login, password) values (?, ?); select * from users where login = ?;'
        self.execute_query(query, login, password, login, is_select=True, is_one=True)
        self.set_user()

