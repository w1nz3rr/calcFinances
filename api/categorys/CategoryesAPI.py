from api.DB.db import *
from api.DB.db_class import *
from datetime import datetime

class CategoryesAPI(DB):
    categoryes = []
    def __init__(self):
        super().__init__()
        self.categoryes = []

    def set_category(self):
        self.error = None
        self.categoryes.clear()
        if self.cache:
            for item in self.cache:
                category = Category()
                category.id, category.name, category.description, category.create_at, category.update_at, category.user_id, category.color = item
                self.categoryes.append(category.__dict__)
        else:
            self.error = 'Нет категорий'

    def get_category(self, id):
        query = 'select * from category where user_id = ?'
        self.execute_query(query, id, is_select=True)
        self.set_category()


    def post_category(self, name, description, user_id):
        query = 'insert into category (name, description, create_at, update_at, user_id) values (?, ?, ?, ?, ?)'
        date = datetime.now()
        self.execute_query(query, name, description, date, date, user_id, is_select=False)
        self.get_category(user_id)

