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

# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# # for (table_name,) in cursor:
# print(tables)



# for product in my_products:

try:
    sql_insert_query = """INSERT INTO nutriscore (nut_id, nut_type) VALUES (NULL,'E' )"""
    # val = ("0")

    mycursor.execute(sql_insert_query)
    cnx.commit()

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

print(mycursor.rowcount, "record inserted.")
