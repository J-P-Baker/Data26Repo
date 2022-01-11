import pyodbc
from pprint import pprint as pp
import pandas as pd
import numpy as np

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
driver = '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password
        ) as docker_northwind:
    with docker_northwind.cursor() as cursor:
        cursor.execute("SELECT * FROM Products")
        row = cursor.fetchall()

        pp(row)

        np_array = np.array(row)
        df = pd.DataFrame(np_array)
        # df = df.drop(0, axis=1)
        pp(df)

        df.to_csv('test_Csv.csv', index=False)

def temp():
    return True



