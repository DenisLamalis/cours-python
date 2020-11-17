import json
import mysql.connector

from data import *
from mysql.connector import errorcode
from db_settings import Database


with open('my_products_fr.json', encoding='utf-8') as json_file:
    my_products = json.load(json_file)

db_settings = Database()
database_name = db_settings.DB_NAME

cnx = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PASSWORD,
    database = db_settings.DB_NAME)

mycursor = cnx.cursor()

try:
    add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (NULL,%s)")
    val = ('A')

    mycursor.execute(add_nutriscore, (val, ))
    cnx.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

print(mycursor.rowcount, "record inserted.")
