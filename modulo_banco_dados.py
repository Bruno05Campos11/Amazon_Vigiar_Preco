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

def InserirNoBanco (volumes):
	print ("\nMÓDULO 3------------------------------------------------------------------------\n")
	tabela = "One_Piece_3_em_1_"
	data = str(date.today()).replace ("-","_")
	tabela = tabela + data

	comando = "CREATE TABLE {} (id int auto_increment primary key, titulo varchar (30) not null, preco tinyint not null, link varchar (30) not null, data date not null);"
	comando = comando.format(tabela)
	maker.execute (comando)

	comando = "INSERT INTO {} (titulo, preco, link, data) VALUES (%s,%s,%s,%s)"
	comando = comando.format (tabela) 
	
	data = str (date.today ())

	for i in volumes:
		valores = (i[0], i[1], i[2], data)
		maker.execute (comando, valores)
		banco.commit ()
		print (maker.rowcount, "foi inserido")

	print ("\nBanco preparado para consultas!")