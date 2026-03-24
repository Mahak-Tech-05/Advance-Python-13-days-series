import mysql.connector #imports the library for the connector 

# create connection 
conn = mysql.connector.connect( # its a variable that holds the connector database  details
    host="localhost",
    user="root",
    password="",
    database = "SANIYA"
)

# check connection
if conn.is_connected(): # you can also implement all the details for the variable while using the variable instead of the connector function 
    print("Connection is successful")

# create cursor 
cursor = conn.cursor() # cursor is used to execute the sql commands
