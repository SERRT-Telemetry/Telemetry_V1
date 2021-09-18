import mysql.connector

user = 'epiz_29758551'  # 'id17488151_esp32_serrt'
password = 'teKA1nXlygs'  # 'solarpower' #'Solarpower2021$'
host = 'sql203.epizy.com'  # 'localhost'  # '48564.us-imm-sql6.000webhost.io'
database = 'epiz_29758551_esp32'  # 'id17488151_esp32'
port = '3306'

cnx = mysql.connector.connect(user=user, password=password, host=host, database=database, port=port)

cnx.close()