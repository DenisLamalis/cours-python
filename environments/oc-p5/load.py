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
        with open('transform_products.json', encoding='utf-8') as json_file:
            self.my_products = json.load(json_file)

    def load_data(self):
        """ """
        print(list(self.my_products.keys()))

        for prod_key in list(self.my_products.keys()):
            # prod_key = list(self.my_products.keys())[3]
            prod_to_load = self.my_products[prod_key]
            # print(prod_to_load)

            # Produits
            if self.tab_produits(prod_key) == False:
                nut_id = self.check_product('nut_id', 'nutriscore', 'nut_type', prod_to_load['nutriscore_grade'][0])          
                add_product = (f"INSERT INTO produits SET prod_id='{prod_key}', prod_nom='{prod_to_load['product_name_fr']}', prod_url='{prod_to_load['url']}', nut_id='{nut_id}'")
            
                self.insert(add_product)
            else:
                print(f"Le produit : {prod_to_load['product_name_fr']}, avec le code : {prod_key}, existe déjà")

            # Categories
            for n in range(len(prod_to_load['categories'])):
                if self.tab_categorie(prod_to_load['categories'][n]) == False:                
                    add_categorie = (f"INSERT INTO categories SET cat_nom='{prod_to_load['categories'][n]}'")
                    self.insert(add_categorie)

                cat_id = self.tab_categorie(prod_to_load['categories'][n])
                check = self.search_id(f"SELECT * FROM prodcat WHERE cat_id='{cat_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodcat = (f"INSERT INTO prodcat SET cat_id='{cat_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodcat)

            # Marques
            for n in range(len(prod_to_load['brands'])):
                if self.tab_marque(prod_to_load['brands'][n]) == False:                
                    add_marque = (f"INSERT INTO marques SET marq_nom='{prod_to_load['brands'][n]}'")
                    self.insert(add_marque)

                marq_id = self.tab_marque(prod_to_load['brands'][n])
                check = self.search_id(f"SELECT * FROM prodmarq WHERE marq_id='{marq_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodmarq = (f"INSERT INTO prodmarq SET marq_id='{marq_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodmarq)

            # Shops
            for n in range(len(prod_to_load['stores'])):
                if self.tab_shop(prod_to_load['stores'][n]) == False:                
                    add_shop = (f"INSERT INTO shops SET shop_nom='{prod_to_load['stores'][n]}'")
                    self.insert(add_shop)

                shop_id = self.tab_shop(prod_to_load['stores'][n])
                check = self.search_id(f"SELECT * FROM prodshop WHERE shop_id='{shop_id}' AND prod_id='{prod_key}' ")
                if not(check):     
                    add_prodshop = (f"INSERT INTO prodshop SET shop_id='{shop_id}', prod_id='{prod_key}' ")
                    self.insert(add_prodshop)


    def tab_categorie(self, value):
        """ """
        id_target = 'cat_id'
        table_target = 'categories'
        column_target = 'cat_nom'
        product_target = value

        result = self.check_product(id_target, table_target, column_target, product_target)
        return result

    def tab_marque(self, value):
        """ """
        id_target = 'marq_id'
        table_target = 'marques'
        column_target = 'marq_nom'
        product_target = value

        result = self.check_product(id_target, table_target, column_target, product_target)
        return result

    def tab_shop(self, value):
        """ """
        id_target = 'shop_id'
        table_target = 'shops'
        column_target = 'shop_nom'
        product_target = value

        result = self.check_product(id_target, table_target, column_target, product_target)
        return result

    def tab_produits(self, value):
        """ """
        id_target = 'prod_id'
        table_target = 'produits'
        column_target = 'prod_id'
        product_target = value

        result = self.check_product(id_target, table_target, column_target, product_target)
        return result

    # def tab_prodcat(self, value):
    #     """ """
    #     id_target = 'prod_id'
    #     table_target = 'prodcat'
    #     column_target = 'prod_id'
    #     product_target = value

    #     result = self.check_product(id_target, table_target, column_target, product_target)
    #     return result


    def check_product(self, id_target, table_target, column_target, product_target):
        """ I Check if a value is in a table, if yes I return its id """
        query = (f"SELECT {id_target} FROM {table_target} WHERE {column_target} LIKE '{product_target}'")
        
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()

        if len(result) < 1:
            return False
        elif len(result) > 1:
            return print("ca va pas")
        else:
            for id in chain.from_iterable(result):
                return id

    def insert(self, query):
        self.mycursor.execute(query)
        self.connection.commit()

    def search_id(self, query):
        self.mycursor.execute(query)
        rows = self.mycursor.fetchall()
        return rows




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
print(loader.load_data())


# try:
#     add_nutriscore = ("INSERT INTO nutriscore (nut_id, nut_type) VALUES (NULL,%s)")
#     val = ('A')

#     mycursor.execute(add_nutriscore, (val, ))
#     cnx.commit()

# except mysql.connector.Error as error:
#     print("Failed to insert into MySQL table {}".format(error))

# print(mycursor.rowcount, "record inserted.")