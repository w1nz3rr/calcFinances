from db import *
from db_class import *


class UserApi(User, DB):

    def get_user(self):
        if self.connect == None:
            self.connect = pyodbc.connect(self.data_connect)

        query = 'select * from users where id = ?'

        self.execute_query(query, self.id, is_select=True)
        return self.data
