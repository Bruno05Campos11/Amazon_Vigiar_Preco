from bs4 import BeautifulSoup as soup
from modulo_pegar_html import ExecutarPegarHtml
from modulo_adicionar_dados import PesquisarDados
from modulo_banco_dados import InserirNoBanco
from modulo_banco_dados import SelecionarPrecos

k = 0
while k != 4:
	print ("\n\tMAIN")
	print ("\t1 - Capturar Html da Amazon")
	print ("\t2 - Pesquisar e inserir dados no banco (execute a função '1' ao menos uma vez)")
	print ("\t3 - Fazer consulta no banco de dados")
	print ("\t4 - Sair")
	k = int (input ("\nSelecione uma função: "))

	if k == 1:
		ExecutarPegarHtml()
	
	elif k == 2:
		x = PesquisarDados() 
		lista_titulos = x[0]
		lista_precos = x[1]
		lista_links = x[2]

		InserirNoBanco (lista_titulos, lista_precos, lista_links)

	elif k == 3:
		SelecionarPrecos()

	elif k == 4:
		print ("Programa Encerrado!")

	else:
		print ("Comando inválido!")