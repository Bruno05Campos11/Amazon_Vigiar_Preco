from bs4 import BeautifulSoup as soup
from modulo_pegar_html import ExecutarPegarHtml
from modulo_adicionar_dados import PesquisarDados
from modulo_criar_banco import InserirNoBanco

#ExecutarPegarHtml()

x = PesquisarDados() 
lista_titulos = x[0]
lista_precos = x[1]
lista_links = x[2]

InserirNoBanco (lista_titulos, lista_precos, lista_links)