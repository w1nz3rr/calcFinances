import pyodbc


class DB:
    data_connect = r'Driver={SQL Server};Server=calculation_finances.mssql.somee.com;Database=calculation_finances;UID=w1nz3rr_SQLLogin_1;PWD=r8u6xqat6y'
    connect = None
    data = None

    def __init__(self):
        self.connect = self.create_connection()

    def create_connection(self):
        self.connect = pyodbc.connect(self.data_connect)

    def execute_query(self, query, *args, is_select=False):
        cursor = self.connect.cursor()
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)

        if is_select:
            self.data = cursor.fetchall()

        cursor.commit()
        cursor.close()
        return True

    def close_connection(self):
        self.connect.close()

