from api.DB.db import *
from api.DB.db_class import *
from datetime import datetime

class One_operationAPI(DB):

    def __init__(self):
        super().__init__()

    def set_operation(self):
        self.operation = Operation()
        if self.cache:
            self.operation.id,  self.operation.type_operation,  self.operation.date,  self.operation.value, \
            self.operation.description,  self.operation.user_id,  self.operation.category_id = self.cache[0]
        else:
            self.error = 'нет операции'

    def get_operation(self, user_id, operation_id):
        self.error = None
        query = 'select * from operation where user_id = ? and id = ?'
        self.execute_query(query, user_id, operation_id, is_select=True)
        self.set_operation()

    def delete_operation(self, user_id, operation_id):
        query = 'delete from operation where user_id = ? and id = ?'
        return self.execute_query(query, user_id, operation_id, is_select=False)

    def put_operation(self, operation_id, type_operation, value, description, user_id):
        query = 'update operation set type_operation = ?, operation_value = ?, description = ? where id = ?'
        self.execute_query(query, type_operation, value, description, operation_id)
        self.get_operation(user_id, operation_id)

