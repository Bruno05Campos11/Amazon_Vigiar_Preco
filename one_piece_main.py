from bs4 import BeautifulSoup as soup
from modulo_pegar_html import ExecutarPegarHtml
from modulo_adicionar_dados import PesquisarDados
from modulo_criar_banco import InserirNoBanco

#ExecutarPegarHtml()

x = PesquisarDados() 
lista_titulos = x[0]
lista_precos = x[1]

InserirNoBanco (lista_titulos, lista_precos)








#sempre que pegar o dado de algum dia criar uma nova tabela
#essa tabela se chamará One_Piece_3_em_1_{data}
#para pegar a data é nescessário uma biblioteca diferenciada
#use format() para efetuar a troca