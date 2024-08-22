from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
from amazoncaptcha import AmazonCaptcha
from time import sleep
import re

def EntrarAmazon (nome):
	print ("\nMÓDULO 1: Pegar HTML--------------------------------------------------------------------\n")
	configuracao = webdriver.EdgeOptions()
	configuracao.add_argument("--start-maximized")
	#configuracao.add_argument("--headless") #para rodar em segundo plano sem abrir o navegador
	navegador = webdriver.Edge(options=configuracao)

	navegador.get ("https://www.amazon.com.br/")
	#navegador.get ("https://www.amazon.com.br/errors/validateCaptcha")
	sleep (2)

	titulo = navegador.title
	if titulo != "Amazon.com.br | Tudo pra você, de A a Z.":
		print ("\nCaptcha não é um problema para nós!")
		sleep (3)

		link = navegador.find_element (By.XPATH, "//div[@class = 'a-row a-text-center']//img").get_attribute('src')
		captcha = AmazonCaptcha.fromlink(link)
		solucao = AmazonCaptcha.solve (captcha)

		pesquisa = navegador.find_element(By.ID, "captchacharacters")
		pesquisa.send_keys (solucao)
		pesquisa.submit()

	sleep (2)
	pesquisa = navegador.find_element (By.XPATH, "//input[@name= 'field-keywords']")
	pesquisa.send_keys(nome)
	pesquisa.submit()

	#preparar para salvar página html como local
	site_atual = soup (navegador.page_source, 'html.parser')
	#print (site_atual.prettify())
	return site_atual

def SalvarLocal(site_soup, nome_banco):
	arquivo = "local_soup_" +nome_banco+ ".html"
	with open (arquivo, "w", encoding = "utf-8") as texto:
		texto.write (site_soup.prettify())

def ExecutarPegarHtml (nome, nome_banco):
	este_site = EntrarAmazon(nome)
	SalvarLocal(este_site, nome_banco)