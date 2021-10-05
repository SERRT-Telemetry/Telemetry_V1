import mysql.connector

user = 'admin'
password = 'Solarpower802'
host = 'serrt-database.c7sgroillrv6.us-east-2.rds.amazonaws.com'
database = 'sensor_data'
port = '3306'

db = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

print("Connected to database!")

db.close()