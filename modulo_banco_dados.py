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

def AdicionarData ():
	dia = str (input ("Dia (se não houver dezena, favor colocar um 0 antes do número): "))
	mes = str (input("Mês (Dia (se não houver dezena, favor colocar um 0 antes do número): "))
	ano = str (input("Ano: "))

	data = ano + "_" +mes+ "_" +dia
	return data

def VerificarExiste (tabela):
	maker.execute ("SHOW TABLES")
	existe = False
	conferir = "('{}',)"
	conferir = conferir.format (tabela)
	
	for i in maker:		
		if conferir == str(i):
			existe = True
	return existe

def SelectComando (tabela1, tabela2):
	comando = "SELECT * FROM {} INNER JOIN {} ON {}.id = {}.id;"
	comando = comando.format (tabela1, tabela2, tabela1, tabela2)
	maker.execute (comando)
	resultado = maker.fetchall()

	for i in resultado:
		print (i)

def SelecionarPrecos ():	
	f = 0
	while f != 7:
		print ("\n\tSELEÇÃO")
		print ("\t5 - Ver o preço de duas datas específicas")
		print ("\t6 - Ver os 5 últimos preços")
		print ("\t7 - Nada não")
		f = int(input("\nSelecione uma função: "))

		if f == 5:
			data1 = AdicionarData ()
			data2 = AdicionarData () 
			
			tabela = "one_piece_3_em_1_"
			tabela1 = tabela + data1
			tabela2 = tabela + data2

			verificar = VerificarExiste (tabela1)
			if verificar == True:
				verificar = VerificarExiste (tabela2)
				if verificar == True:
					if tabela1 == tabela2:
						print ("Não vale datas iguais!")
					else:
						SelectComando(tabela1, tabela2)
				else:
					print ("A segunda data não está cadastrada no banco de dados")
			else:
				print ("A primeira data não está cadastrada no banco de dados")
		
		elif f == 6:
			print ("6")

		elif f == 7:
			print ("Progrma Encerrado!")
