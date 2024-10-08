import mysql.connector as db
from datetime import date

#"SelecionarPrecos()" é a última função do arquivo

def InserirNoBanco (volumes, nome_banco):
	print ("\nMÓDULO 3: Banco de Dados---------------------------------------------------------\n")
	#Conexão com o banco
	banco = db.connect (
		host= "127.0.0.1",
		user = "root",
		password = "1234",
		database = nome_banco
	)
	maker = banco.cursor ()

	#Preparando nova tabela com a data de hoje
	tabela = nome_banco
	data = str(date.today()).replace ("-","_")
	tabela = tabela + data

	#Criando nova tabela
	comando = "CREATE TABLE {} (id int auto_increment primary key, titulo varchar (105) not null, preco decimal (5,2) not null, link varchar (30) not null, data date not null);"
	comando = comando.format(tabela)
	maker.execute (comando)

	#Inserindo valores na tabela
	comando = "INSERT INTO {} (titulo, preco, link, data) VALUES (%s,%s,%s,%s)"
	comando = comando.format (tabela) 
	
	data = str (date.today ())

	#Armazenando no banco de dados cada volume com seus respectivos valores
	for i in volumes:
		valores = (i[0], i[1], i[2], data)
		maker.execute (comando, valores)
		banco.commit ()
		print (maker.rowcount, "foi inserido")

	print ("\nBanco preparado para consultas!")