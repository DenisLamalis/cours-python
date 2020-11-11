from data import *
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'PureBeurre'

TABLES = {}
TABLES['categories'] = (
    "CREATE TABLE `categories` ("
    "  `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `cat_nom` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`cat_id`)"
    ") ENGINE=InnoDB")

TABLES['nutriscore'] = (
    "CREATE TABLE `nutriscore` ("
    "  `nut_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nut_type` char(1) NOT NULL,"
    "  PRIMARY KEY (`nut_id`)"
    ") ENGINE=InnoDB")

TABLES['nutriscore'] = (
    "CREATE TABLE `nutriscore` ("
    "  `nut_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nut_type` char(1) NOT NULL,"
    "  PRIMARY KEY (`nut_id`)"
    ") ENGINE=InnoDB")



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

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
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

