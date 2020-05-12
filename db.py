import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin',
)

cursor = db.cursor()

cursor.execute('CREATE DATABASE kalamburyzawody')

db = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin',
    database='kalamburyzawody'
)

cursor = db.cursor()

cursor.execute("CREATE TABLE  `hasla` (\
	`id` int(10) NOT NULL auto_increment,\
	`tresc` varchar(255) NOT NULL,\
	`kategoria` varchar(255) NOT NULL,\
	PRIMARY KEY( `id` ),\
    UNIQUE(tresc)\
);")

cursor.execute("CREATE TABLE `zawodnicy` (\
	`id` INT NOT NULL AUTO_INCREMENT,\
	`imie` VARCHAR NOT NULL,\
	`nazwisko` VARCHAR NOT NULL,\
	`numer` INT NOT NULL,\
	PRIMARY KEY (`id`)\
);")
