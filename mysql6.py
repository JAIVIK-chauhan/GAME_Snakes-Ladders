import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='2007',database='jaivik')

cur=mydb.cursor()

s="CREATE TABLE winner(name varchar(20),coin integer(4))"

cur.execute(s)

