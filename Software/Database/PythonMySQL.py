import mysql.connector

user = 'Administrator'
password = 'Solarpower802'
host = 'serrt-database.c7sgroillrv6.us-east-2.rds.amazonaws.com'
database = 'serrt-database'
port = '3306'

db = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

print("Connected to database!")

# get cursor object
cursor= db.cursor()
  
# execute your query
cursor.execute("SELECT * FROM SensorData")
  
# fetch all the matching rows 
result = cursor.fetchall()
  
# loop through the rows
for row in result:
    print(row)
    print("\n")

cursor.close()
db.close()