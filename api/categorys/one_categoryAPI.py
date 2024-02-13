from api.DB.db import *
from api.DB.db_class import *
from datetime import datetime


class One_categoryAPI(DB):

    def __init__(self):
        super().__init__()

    def set_category(self):
        self.category = Category()
        if self.cache:
            self.category.id, self.category.name, self.category.description, self.category.create_at, \
                self.category.update_at, self.category.user_id, self.category.color = self.cache[0]
        else:
            self.error = 'Нет категории'

    def get_category(self, id, category_id):
        self.error = None
        query = 'select * from category where user_id = ? and id = ?'
        self.execute_query(query, id, category_id, is_select=True)
        self.set_category()

    def delete_category(self, id, category_id):
        query = 'delete from category where user_id = ? and id = ?'
        return self.execute_query(query, id, category_id, is_select=False)

    def put_category(self, id, user_id, name, description, color):
        query = 'update category set name = ?, description = ?, color = ? where id = ?'
        self.execute_query(query, name, description, color, id, is_select=False)
        self.get_category(user_id, id)
