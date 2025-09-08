#pip install mysql-connector-python
#pip install pymysql

import mysql.connector
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='config'
)

conn = mysql.connector.connect(host='localhost',
    user='root',
    password='root',
    database='config')

cur = conn.cursor()
# cur.execute("SELECT * from testdata")
# records = cur.fetchall()
# print(records)
cur.execute("update testdata set is_active='true' where username='admin'")
conn.commit()

cur.close()
conn.close()