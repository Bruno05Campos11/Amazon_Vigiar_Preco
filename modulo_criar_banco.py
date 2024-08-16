import mysql.connector as db
#from bs4 import BeautifulSoup as soup

def InserirNoBanco (lista_titulos,lista_precos):
	print ("\nMÓDULO 3------------------------------------------------------------------------\n")
	banco = db.connect (
		host= "127.0.0.1",
		user = "root",
		password = "1234",
		database = "one_piece"
	)

	maker = banco.cursor ()

	maker.execute ("CREATE TABLE Volumes (id int auto_increment primary key, titulo varchar (30) not null, preco varchar (14) not null);")
	
	comando = "INSERT INTO Volumes (titulo, preco) VALUES (%s,%s)" 
	x = 0
	for i in lista_titulos:
		valores = (lista_titulos [x], lista_precos [x])
		maker.execute (comando, valores)
		banco.commit ()
		print (maker.rowcount, "foi inserido")
		x += 1
