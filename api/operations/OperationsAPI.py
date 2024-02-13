from api.DB.db import *
from api.DB.db_class import *
from datetime import datetime

class OperationsAPI(DB):

    def __init__(self):
        super().__init__()
        self.operations = []

    def set_operations(self):
        self.operations.clear()
        if self.cache:
            for item in self.cache:
                operation = Operation()
                operation.id, operation.type_operation, operation.date, operation.value, operation.description, operation.user_id, operation.category_id = item
                self.operations.append(operation.__dict__)
        else:
            self.error = 'Нет операций'

    def get_operation(self, user_id, category_id):
        query = 'select * from operation where user_id = ? and category_id = ?'
        self.execute_query(query, user_id, category_id, is_select=True)
        self.set_operations()

    def post_operation(self, type_operation, value, description, user_id, category_id):
        query = 'insert into operation (type_operation, date, value, description, user_id, category_id) values (?, ?, ?, ?, ?, ?)'
        date = datetime.now()
        self.execute_query(query, type_operation, date, value, description, user_id, category_id, is_select=False)
        self.get_operation(user_id, category_id)