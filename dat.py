import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="w@2915djkq#",database="store")
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("conection is Sucessfull!!!")