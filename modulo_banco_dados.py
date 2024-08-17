import mysql.connector as db
from datetime import date

#"SelecionarPrecos()" é a última função do arquivo

#conexão com o banco
banco = db.connect (
	host= "127.0.0.1",
	user = "root",
	password = "1234",
	database = "one_piece"
)
maker = banco.cursor ()

def InserirNoBanco (lista_titulos,lista_precos, lista_links):
	print ("\nMÓDULO 3------------------------------------------------------------------------\n")
	tabela = "One_Piece_3_em_1_"
	data = str(date.today()).replace ("-","_")
	tabela = tabela + data

	comando = "CREATE TABLE {} (id int auto_increment primary key, titulo varchar (30) not null, preco varchar (14) not null, link varchar (30) not null, data date not null);"
	comando = comando.format(tabela)
	maker.execute (comando)

	comando = "INSERT INTO {} (titulo, preco, link, data) VALUES (%s,%s,%s,%s)"
	comando = comando.format (tabela) 
	
	data = str (date.today ())

	x = 0
	for i in lista_titulos:
		valores = (lista_titulos[x], lista_precos[x], lista_links[x], data)
		maker.execute (comando, valores)
		banco.commit ()
		print (maker.rowcount, "foi inserido")
		x += 1