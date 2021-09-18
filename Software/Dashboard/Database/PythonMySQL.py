import mysql.connector

user = 'telemetry'  # 'id17488151_esp32_serrt'
password = 'solarpower'  # 'solarpower' #'Solarpower2021$'
host = 'db4free.net'  # 'localhost'  # '48564.us-imm-sql6.000webhost.io'
database = 'esp32data'  # 'id17488151_esp32'
port = '3306'

cnx = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

print("Connected to " + database)

cnx.close()