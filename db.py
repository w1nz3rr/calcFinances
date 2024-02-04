import pyodbc


class DB:
    data_connect = r'Driver={SQL Server};Server=calculation_finances.mssql.somee.com;Database=calculation_finances;UID=w1nz3rr_SQLLogin_1;PWD=r8u6xqat6y'
    connect = None
    cursor = None
    cache = None


    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.connect = pyodbc.connect(self.data_connect)
        self.cursor = self.connect.cursor()


    def execute_query(self, query, *args, is_select=False):
        if not self.execute_cursor(query, args):
            return False
        self.cursor.commit()
        if is_select:
            return self.select()

        return True


    def execute_cursor(self, query, args):
        try:
            if args:
                self.cursor.execute(query, args)
            else:
                self.cursor.execute(query)
            return True
        except:
            return False


    def select(self):
        try:
            self.cache = self.cursor.fetchall()
            if len(self.cache) == 1:
                self.cache = self.cache[0]
            return True
        except:
            return False



    def close_connection(self):
        self.cursor.close()
        self.connect.close()


