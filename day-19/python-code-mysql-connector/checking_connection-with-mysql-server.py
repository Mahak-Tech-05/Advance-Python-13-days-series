import mysql.connector

# create connection 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

# check connection
if conn.is_connected():
    print("Connection is successful")

# create cursor
cursor = conn.cursor()
