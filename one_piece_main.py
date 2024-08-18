from bs4 import BeautifulSoup as soup
from modulo_pegar_html import ExecutarPegarHtml
from modulo_adicionar_dados import PesquisarDados
from modulo_banco_dados import InserirNoBanco

k = 0
while k != 5:
	print ("\n\t\t\tMAIN")
	print ("\t\t\t1 - Capturar Html da Amazon")
	print ("\t\t\t2 - Pesquisar dados (execute a função '1' ao menos uma vez)")
	print ("\t\t\t3 - Pesquisar e Inseri-los no banco")
	print ("\t\t\t4 - Executar tudo")
	print ("\t\t\t5 - Sair")
	k = int (input ("\nSelecione uma função: "))


	if k == 1:
		ExecutarPegarHtml()

	elif k == 2:
		x = PesquisarDados() 
		lista_titulos = x[0]
		lista_precos = x[1]
		lista_links = x[2]
	
	elif k == 3:
		x = PesquisarDados() 
		lista_titulos = x[0]
		lista_precos = x[1]
		lista_links = x[2]

		InserirNoBanco (lista_titulos, lista_precos, lista_links)

	elif k == 4:
		ExecutarPegarHtml()

		x = PesquisarDados() 
		lista_titulos = x[0]
		lista_precos = x[1]
		lista_links = x[2]

		InserirNoBanco (lista_titulos, lista_precos, lista_links)

	elif k == 5:
		print ("Programa Encerrado!")

	else:
		print ("Comando inválido!")