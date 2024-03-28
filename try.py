import mysql.connector

conn = mysql.connector.connect(
    user ='root',
    password = 'nyongesa628',
    host = 'localhost',
    database = 'flxdb',
)

cursor = conn.cursor()
cursor.execute('SELECT DATABASE()')

data = cursor.fetchone()
print('connection established to: ', data)
conn.close()