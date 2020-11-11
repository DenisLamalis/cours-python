from data import *
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'PureBeurre'

cnx = mysql.connector.connect(
    host = HOST,
    user = USER,
    password = PASSWORD)

cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

print(create_database(cursor))