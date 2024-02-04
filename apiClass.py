from db import *
from db_class import *


class UserAPI(DB):
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
        self.execute_query(query, id, is_select=True)
        self.set_user()


    def post_user(self, login, password):
        query = f'insert into users (login, password) values (?, ?); select * from users where login = ?;'
        self.execute_query(query, login, password, login, is_select=True)
        self.set_user()


class CategoryAPI(DB):
    category = []
    def __init__(self):
        super().__init__()
        category = []

    def get_category(self, id):
        query = 'select * from category where user_id = ?'
        self.set_category()

    def post_category(self, name, description, user_id):
        query = 'insert into category (name, description, user_id) values (?, ?, ?); select * from category where user_id = ?'
        self.execute_query(query, name, description, user_id, is_select=True)
        self.set_category()

    def set_category(self):
        if self.cache:
            for item in self.cache:
                category = Category()
                category.id, category.name, category.description, category.create_at, category.update_at, category.user_id = item
                self.category.append(category)
        else:
            self.category = 'Нет категорий'