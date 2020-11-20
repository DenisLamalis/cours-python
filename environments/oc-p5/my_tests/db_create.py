from data import *
import mysql.connector
from mysql.connector import errorcode
from db_settings import Database

db_settings = Database()

# Connection and cursor creation

cnx = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PASSWORD)

cursor = cnx.cursor()

# Create the database if not exist

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_settings.DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Open the database

try:
    cursor.execute("USE {}".format(db_settings.DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(db_settings.DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(db_settings.DB_NAME))
        cnx.database = db_settings.DB_NAME
    else:
        print(err)
        exit(1)

# Create tables

for table_name in db_settings.TABLES:
    table_description = db_settings.TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


cursor.close()
cnx.close()

