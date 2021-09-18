import mysql.connector

user = 'telemetry'  # 'id17488151_esp32_serrt'
password = 'solarpower'  # 'solarpower' #'Solarpower2021$'
host = 'db4free.net'  # 'localhost'  # '48564.us-imm-sql6.000webhost.io'
database = 'esp32data'  # 'id17488151_esp32'
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