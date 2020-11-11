from data import *
import mysql.connector

mydb = mysql.connector.connect(
  host = HOST,
  user = USER,
  password = PASSWORD
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE PureBeurre CHARACTER SET 'utf8'")



