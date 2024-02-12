from api.DB.db import DB
from api.DB.db_class import User
from datetime import datetime


class UserAPI(DB):
    user: User

    def __init__(self):
        super().__init__()
        self.user = User()

    def set_user(self):
        print('cache:', self.cache)
        if self.cache:
            self.user.id, self.user.login, self.user.password, self.user.create_at, self.user.update_at, self.user.nickname = \
            self.cache[0]
        else:
            self.error = f'Нет такого пользователя'

    def get_user(self, id):
        query = 'select * from users where id = ?'
        self.execute_query(query, id, is_select=True)
        self.set_user()

    def delete_user(self, id):
        query = 'delete from users where id = ?'
        return self.execute_query(query, id, is_select=False)

    def put_user(self, id, nickname):
        query = 'update users set nickname = ?, update_at = ? where id = ?'
        if self.execute_query(query, nickname, datetime.now(), id, is_select=False):
            self.get_user(id)
        else:
            self.error = 'Ошибка изменения'
