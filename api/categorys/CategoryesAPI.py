from api.DB.db import *
from api.DB.db_class import *
from datetime import datetime

class CategoryesAPI(DB):
    categoryes = []
    def __init__(self):
        super().__init__()
        categoryes = []

    def set_category(self):
        self.categoryes.clear()
        if self.cache:
            for item in self.cache:
                category = Category()
                category.id, category.name, category.description, category.create_at, category.update_at, category.user_id, category.color = item
                self.categoryes.append(category.__dict__)
        else:
            self.categoryes = 'Нет категорий'

    def get_category(self, id):
        query = 'select * from category where user_id = ?'
        self.execute_query(query, id, is_select=True)

        self.set_category()


    def post_category(self, name, description, user_id):
        query = 'insert into category (name, description, user_id) values (?, ?, ?)'
        self.execute_query(query, name, description, user_id, is_select=False)
        self.get_category(user_id)

