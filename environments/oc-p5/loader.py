import json
import mysql.connector

from data import *
from mysql.connector import errorcode
from db_settings import Database

from itertools import chain


class Loader:

    def __init__(self):
        self.db_settings = Database()
        self.db_connect()
        self.open_json()

    def db_connect(self):

        try:
            self.db_settings = Database()
            database_name = self.db_settings.DB_NAME

            self.connection = mysql.connector.connect(
                host = HOST,
                user = USER,
                password = PASSWORD,
                database = database_name)

            self.mycursor = self.connection.cursor()

            if (self.connection.is_connected()):
                print(f"Connection à la base {database_name} : OK")

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

    def db_disconnect(self):
            if (connection.is_connected()):
                mycursor.close()
                connection.close()
                print("MySQL connection is closed")
        

    def open_json(self):
        with open('my_products_fr.json', encoding='utf-8') as json_file:
            self.my_products = json.load(json_file)

    def load_data(self):

        first_key = list(self.my_products.keys())[0]
        product_test = self.my_products[first_key]

        print(product_test)

    def check_product(self, id_target, table_target, column_target, product_target):
        
        query = (f"SELECT {id_target} FROM {table_target} WHERE {column_target} LIKE '{product_target}'")
        
        self.mycursor.execute(query)

        output = self.mycursor.fetchall()

        if len(output) < 1:
            return False
        elif len(output) > 1:
            return print("ca va pas")
        else:
            for id in chain.from_iterable(output):
                id = id
            return id


    def load_nutriscore(self):

        try:
            add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (%s,%s)")
            values = (1, 'A')
            self.mycursor.execute(add_nutriscore, values)
            values = (2, 'B')
            self.mycursor.execute(add_nutriscore, values)      
            values = (3, 'C')
            self.mycursor.execute(add_nutriscore, values) 
            values = (4, 'D')
            self.mycursor.execute(add_nutriscore, values) 
            values = (5, 'E')
            self.mycursor.execute(add_nutriscore, values) 
            
            self.connection.commit()

            print("Les différents Nutriscore ont été chargés dans la base.")

        except mysql.connector.Error as error:
            print("Erreur lors du chargement : {}".format(error))


# ============================================================

if __name__ == "__main__":
    loader = Loader()

# loader.open_json()
loader.check_product('nut_id', 'nutriscore', 'nut_type', 'J')


# try:
#     add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (NULL,%s)")
#     val = ('A')

#     mycursor.execute(add_nutriscore, (val, ))
#     cnx.commit()

# except mysql.connector.Error as error:
#     print("Failed to insert into MySQL table {}".format(error))

# print(mycursor.rowcount, "record inserted.")
