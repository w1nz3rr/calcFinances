from api.DB.db import *
from api.DB.db_class import *

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