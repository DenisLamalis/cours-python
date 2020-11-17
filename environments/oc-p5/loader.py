import json
import mysql.connector

from data import *
from mysql.connector import errorcode
from db_settings import Database


class Loader:

    def __init__(self):
        pass

    def db_connect(self):

        try:
            db_settings = Database()
            database_name = db_settings.DB_NAME

            self.connection = mysql.connector.connect(
                host = HOST,
                user = USER,
                password = PASSWORD,
                database = db_settings.DB_NAME)

            mycursor = connection.cursor()

            if (connection.is_connected()):
                print("Connection : OK")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

    def db_disconnect(self):
            if (connection.is_connected()):
                mycursor.close()
                connection.close()
                print("MySQL connection is closed")
        

    def open_json(self):
        with open('my_products_fr.json', encoding='utf-8') as json_file:
            my_products = json.load(json_file)

        print(my_products)

    def load_data(self):
        pass


if __name__ == "__main__":
    loader = Loader()

# loader.open_json()
loader.db_disconnect()


# try:
#     add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (NULL,%s)")
#     val = ('A')

#     mycursor.execute(add_nutriscore, (val, ))
#     cnx.commit()

# except mysql.connector.Error as error:
#     print("Failed to insert into MySQL table {}".format(error))

# print(mycursor.rowcount, "record inserted.")
