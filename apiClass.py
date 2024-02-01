from db import *
from db_class import *


class UserApi(User, DB):
    user: User


    def __init__(self):
        super().__init__()
        self.user = User()


    def get_user(self, id):
        query = 'select * from users where id = ?'
        self.execute_query(query, id, is_select=True, is_one=True)
        if self.cache:
            self.user.id, self.user.login, self.user.password, self.user.create_at, self.user.update_at = self.cache
        else:
            self.user = f'Нет такого пользователя'



