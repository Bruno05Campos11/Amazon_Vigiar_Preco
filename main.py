from bs4 import BeautifulSoup as soup
from modulo_pegar_html import ExecutarPegarHtml
from modulo_adicionar_dados import PesquisarDados
from modulo_banco_dados import InserirNoBanco
from classe_manga import Obra

def EscolherManga():
	k = 0
	while k < 1 or k > 5:
		print ("\t\t\t1 - One Piece 3 em 1")
		print ("\t\t\t2 - Jojo parte 4")
		print ("\t\t\t3 - Scott Pilgrim")
		print ("\t\t\t4 - Takagi-san")
		print ("\t\t\t5 - Almanaque Guará")
		k = int (input ("\nSELECIONE UMA OBRA: "))

		if k == 1:
			obra = Obra ("One Piece 3 em 1", "One Piece 3 em 1", "One Piece (3 em 1)", "One_Piece_3_em_1_")

		elif k == 2:
			obra = Obra("Jojo parte 4", "Diamond is Unbreakable", "Diamond is Unbreakable", "Jojo_parte_4_")

		elif k == 3:
			obra = Obra("Scott Pilgrim", "- Contra O Mundo -", "- Contra O Mundo -" ,"Scott_Pilgrim_")

		elif k == 4:
			obra = Obra("Takagi san", "A Mestra Das Pegadinhas", "A Mestra Das Pegadinhas", "Takagi_san_")

		elif k == 5:
			obra = Obra("Almanaque Guará", "Almanaque Guar", "Almanaque Guar",  "Almanaque_Guara_")

		else:
			print ("Comando inválido!")

		return obra

def Menu(obra):
	k = 0
	while k != 10:
		print ("\n\t\t\tMAIN")
		print ("\t\t\t6 - Capturar Html da Amazon")
		print ("\t\t\t7 - Pesquisar dados (execute a função '1' ao menos uma vez)")
		print ("\t\t\t8 - Pesquisar e Inseri-los no banco")
		print ("\t\t\t9 - Executar tudo")
		print ("\t\t\t10 - Sair")
		k = int (input ("\nSELECIONE UMA FUNÇÃO: "))


		if k == 6:
			ExecutarPegarHtml (obra.nome, obra.banco)

		elif k == 7:
			dados = PesquisarDados (obra.buscador, obra.alternativo, obra.banco) 
		
		elif k == 8:
			dados = PesquisarDados (obra.buscador, obra.alternativo, obra.banco)
			InserirNoBanco (dados, obra.banco)

		elif k == 9:
			ExecutarPegarHtml (obra.nome, obra.banco)
			dados = PesquisarDados (obra.buscador, obra.alternativo, obra.banco)
			InserirNoBanco (dados, obra.banco)

		elif k == 10:
			print ("Programa Encerrado!")

		else:
			print ("Comando inválido!")

#---------------------------------------------------------------------------------------------------------
opcao = EscolherManga()
Menu(opcao)