
class Database:

    def __init__(self):

        self.DB_NAME = 'PureBeurre'

        self.TABLES = {}

        self.TABLES['categories'] = (
            "CREATE TABLE IF NOT EXISTS `categories` ("
            "  `cat_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `cat_nom` varchar(100) NOT NULL,"
            "  PRIMARY KEY (`cat_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['shop'] = (
            "CREATE TABLE IF NOT EXISTS `shop` ("
            "  `shop_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `shop_nom` varchar(150) NOT NULL,"
            "  PRIMARY KEY (`shop_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['marques'] = (
            "CREATE TABLE IF NOT EXISTS `marques` ("
            "  `marq_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `marq_nom` varchar(150) NOT NULL,"
            "  PRIMARY KEY (`marq_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['nutriscore'] = (
            "CREATE TABLE IF NOT EXISTS `nutriscore` ("
            "  `nut_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `nut_type` char(1) NOT NULL,"
            "  PRIMARY KEY (`nut_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['produits'] = (
            "CREATE TABLE IF NOT EXISTS `produits` ("
            "  `prod_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `prod_nom` varchar(150) NOT NULL,"
            "  `prod_code` int NOT NULL,"
            "  `prod_url` varchar(150) NOT NULL,"
            "  `prod_store` varchar(150) NULL,"
            "  `cat_id` int(11) NOT NULL,"
            "  `nut_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prod_id`),"
            "  CONSTRAINT `fk_prodcat_id` FOREIGN KEY (`cat_id`) "
            "     REFERENCES `categories` (`cat_id`),"
            "  CONSTRAINT `fk_nut_id` FOREIGN KEY (`nut_id`) "
            "     REFERENCES `nutriscore` (`nut_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['sauvegardes'] = (
            "CREATE TABLE IF NOT EXISTS`sauvegardes` ("
            "  `save_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `prod_id` int(11) NOT NULL,"
            "  `save_time` datetime NOT NULL,"
            "  PRIMARY KEY (`save_id`),"
            "  CONSTRAINT `fk_saveprod_id` FOREIGN KEY (`prod_id`) "
            "     REFERENCES `produits` (`prod_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['prodcat'] = (
            "CREATE TABLE IF NOT EXISTS `prodcat` ("
            "  `prodcat_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `cat_id` int(11) NOT NULL,"
            "  `prod_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prodcat_id`),"
            "  CONSTRAINT `fk_cat_id` FOREIGN KEY (`cat_id`) "
            "     REFERENCES `categories` (`cat_id`),"
            "  CONSTRAINT `fk_prodcatprod_id` FOREIGN KEY (`prod_id`) "
            "     REFERENCES `produits` (`prod_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['prodshop'] = (
            "CREATE TABLE IF NOT EXISTS `prodshop` ("
            "  `prodshop_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `shop_id` int(11) NOT NULL,"
            "  `prod_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prodshop_id`),"
            "  CONSTRAINT `fk_shop_id` FOREIGN KEY (`shop_id`) "
            "     REFERENCES `shop` (`shop_id`),"
            "  CONSTRAINT `fk_prodshopprod_id` FOREIGN KEY (`prod_id`) "
            "     REFERENCES `produits` (`prod_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['prodmarq'] = (
            "CREATE TABLE IF NOT EXISTS `prodmarq` ("
            "  `prodmarq_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `marq_id` int(11) NOT NULL,"
            "  `prod_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prodmarq_id`),"
            "  CONSTRAINT `fk_marq_id` FOREIGN KEY (`marq_id`) "
            "     REFERENCES `marques` (`marq_id`),"
            "  CONSTRAINT `fk_prodmarqprod_id` FOREIGN KEY (`prod_id`) "
            "     REFERENCES `produits` (`prod_id`)"
            ") ENGINE=InnoDB")

    def view_db(self):
        print(self.DB_NAME)
