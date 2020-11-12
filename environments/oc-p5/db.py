
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

        self.TABLES['nutriscore'] = (
            "CREATE TABLE IF NOT EXISTS `nutriscore` ("
            "  `nut_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `nut_type` char(1) NOT NULL,"
            "  PRIMARY KEY (`nut_id`)"
            ") ENGINE=InnoDB")

        self.TABLES['marques'] = (
            "CREATE TABLE IF NOT EXISTS `marques` ("
            "  `mar_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `mar_nom` varchar(150) NOT NULL,"
            "  `prodfab_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`mar_id`)"
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
            "  `prodfab_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prod_id`),"
            "  CONSTRAINT `fk_cat_id` FOREIGN KEY (`cat_id`) "
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

        self.TABLES['prodfab'] = (
            "CREATE TABLE IF NOT EXISTS `prodfab` ("
            "  `prodfab_id` int(11) NOT NULL AUTO_INCREMENT,"
            "  `mar_id` int(11) NOT NULL,"
            "  `prod_id` int(11) NOT NULL,"
            "  PRIMARY KEY (`prodfab_id`),"
            "  CONSTRAINT `fk_mar_id` FOREIGN KEY (`mar_id`) "
            "     REFERENCES `marques` (`mar_id`),"
            "  CONSTRAINT `fk_prodfabprod_id` FOREIGN KEY (`prod_id`) "
            "     REFERENCES `produits` (`prod_id`)"
            ") ENGINE=InnoDB")