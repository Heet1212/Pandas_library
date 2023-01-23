import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin")
print(mydb)    
cursor=mydb.cursor()
cursor.execute("SHOW DATABASEs;")
for i in cursor:
    print(i)