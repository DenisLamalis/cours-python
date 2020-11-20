from config import *
import mysql.connector
from mysql.connector import errorcode

class Database:
    """ """

    def __init__(self):
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = 'purebeurre'

    def connection(self):
        """ """

        try:
            self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database)

            self.mycursor = self.connection.cursor()

            if (self.connection.is_connected()):
                print(f"Connection à la base {self.database} : OK")

        except mysql.connector.Error as error:
            print("Echec : impossible de me connecté, {}".format(error))


if __name__ == "__main__":
    database = Database()

# database.connection()