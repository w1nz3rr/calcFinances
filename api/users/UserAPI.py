from api.DB.db import DB
from api.DB.db_class import User

class UserAPI(DB):
    user: User

    def __init__(self):
        super().__init__()
        self.user = User()

    def set_user(self):
        if self.cache:
            self.user.id, self.user.login, self.user.password, self.user.create_at, self.user.update_at = self.cache[0]
        else:
            self.user = f'Нет такого пользователя'


    def get_user(self, id):
        query = 'select * from users where id = ?'
        self.execute_query(query, id, is_select=True)
        self.set_user()