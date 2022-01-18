import pyodbc
import squarify


class NwProducts:

    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.docker_northwind = pyodbc.connect('DRIVER=' + self.driver + ';SERVER=tcp:' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_products_records(self):
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)


    def avarage_unit_price(self):
        total =[]
        query_records = self._sql_query("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            total.append(record.UnitPrice)
        print(sum(total) / len(total))