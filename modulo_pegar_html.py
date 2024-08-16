from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
from time import sleep
import re

def EntrarAmazon ():
	print ("\nMÓDULO 1------------------------------------------------------------------------\n")
	configuracao = webdriver.EdgeOptions()
	configuracao.add_argument("--start-maximized")
	#configuracao.add_argument("--headless") #para rodar em segundo plano sem abrir o navegador
	navegador = webdriver.Edge(options=configuracao)

	navegador.get ("https://www.amazon.com.br/")
	#navegador.delete_all_cookies()
	sleep (2)

	titulo = navegador.title
	if titulo != "Amazon.com.br | Tudo pra você, de A a Z.":
		print ("\nNos deparamos com Captcha")
		quit()

	pesquisa = navegador.find_element (By.XPATH, "//input[@name= 'field-keywords']")
	pesquisa.send_keys("One Piece 3 em 1")
	pesquisa.submit()

	#preparar para salvar página html como local
	site_atual = soup (navegador.page_source, 'html.parser')
	#print (site_atual.prettify())
	return site_atual

def SalvarLocal(site_soup):
	with open ("local_soup_html.html", "w", encoding = "utf-8") as texto:
		texto.write (site_soup.prettify())

def ExecutarPegarHtml ():
	este_site = EntrarAmazon()
	SalvarLocal(este_site)