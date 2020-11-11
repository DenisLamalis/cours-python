from data import *
import mysql.connector
from mysql.connector import errorcode


# Settings

DB_NAME = 'PureBeurre'

TABLES = {}
TABLES['categories'] = (
    "CREATE TABLE IF NOT EXISTS `categories` ("
    "  `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `cat_nom` varchar(100) NOT NULL,"
    "  PRIMARY KEY (`cat_id`)"
    ") ENGINE=InnoDB")

TABLES['nutriscore'] = (
    "CREATE TABLE IF NOT EXISTS `nutriscore` ("
    "  `nut_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `nut_type` char(1) NOT NULL,"
    "  PRIMARY KEY (`nut_id`)"
    ") ENGINE=InnoDB")

TABLES['marques'] = (
    "CREATE TABLE IF NOT EXISTS `marques` ("
    "  `mar_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `mar_nom` varchar(150) NOT NULL,"
    "  `prodfab_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`mar_id`),"
    "  CONSTRAINT `fk_prodfab_id` FOREIGN KEY (`prodfab_id`) "
    "     REFERENCES `prodfab` (`prodfab_id`)"
    ") ENGINE=InnoDB")

TABLES['prodfab'] = (
    "CREATE TABLE IF NOT EXISTS `prodfab` ("
    "  `prodfab_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `mar_id` int(11) NOT NULL,"
    "  `prod_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`prodfab_id`),"
    "  CONSTRAINT `fk_mar_id` FOREIGN KEY (`mar_id`) "
    "     REFERENCES `marques` (`mar_id`),"
    "  CONSTRAINT `fk_prod_id` FOREIGN KEY (`prod_id`) "
    "     REFERENCES `produits` (`prod_id`)"
    ") ENGINE=InnoDB")

TABLES['produits'] = (
    "CREATE TABLE IF NOT EXISTS `produits` ("
    "  `prod_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `prod_nom` varchar(150) NOT NULL,"
    "  `prod_code` int NOT NULL,"
    "  `prod_url` varchar(150) NOT NULL,"
    "  `prod_store` varchar(150) NULL,"
    "  `cat_id` int(11) NOT NULL,"
    "  `nut_id` int(11) NOT NULL,"
    "  `prodfab_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`prod_id`),"
    "  CONSTRAINT `fk_cat_id` FOREIGN KEY (`cat_id`) "
    "     REFERENCES `categories` (`cat_id`),"
    "  CONSTRAINT `fk_nut_id` FOREIGN KEY (`nut_id`) "
    "     REFERENCES `nutriscore` (`nut_id`),"
    "  CONSTRAINT `fk_prodfab_id` FOREIGN KEY (`prodfab_id`) "
    "     REFERENCES `prodfab` (`prodfab_id`)"
    ") ENGINE=InnoDB")

TABLES['sauvegardes'] = (
    "CREATE TABLE IF NOT EXISTS`sauvegardes` ("
    "  `save_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `prod_id` int(11) NOT NULL,"
    "  `save_time` datetime NOT NULL,"
    "  PRIMARY KEY (`save_id`),"
    "  CONSTRAINT `fk_prod_id` FOREIGN KEY (`prod_id`) "
    "     REFERENCES `produits` (`prod_id`)"
    ") ENGINE=InnoDB")


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
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Open the database

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

# Create tables

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

