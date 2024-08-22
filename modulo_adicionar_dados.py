from bs4 import BeautifulSoup as soup
import pyshorteners

def PesquisarDados (nome_buscador, nome_alternativo, nome_banco):
	print ("\nMÓDULO 2: Adicionar Dados--------------------------------------------------------------\n")
	#Construindo um objeto Beautiful Soup
	arquivo = "C:/Users/erick/Documents/codes/Amazon_Vigiar_Preco/local_soup_"+nome_banco+".html"
	endereco = open (arquivo, "r", encoding = "utf-8")
	site = endereco.read()
	local_soup = soup(site, 'html.parser')	

	#Pesquisando os valores de título, preço e link de cada volume da obra
	volumes = []

	cards = local_soup.find_all ("div", class_="puis-card-container")
	for card in cards:
		titulo = card.find ("span", class_= "a-size-base-plus").get_text().strip()
		preco = card.find ("span", class_= "a-offscreen")
		if preco != None:
			try:
				preco = float(preco.get_text().replace(".", "").replace(",",".").strip()[3:])
			except:
				break
		else:
			preco = float()
		link = card.find ("a", class_= "a-link-normal s-no-outline")
		link = "https://www.amazon.com.br" + link["href"]
		link_encurtado = pyshorteners.Shortener().tinyurl.short (link)

		#Adicionar na lista o volume coletado com todos os valores 
		if nome_buscador.upper() in titulo.upper() or nome_alternativo.upper() in titulo.upper():
			volumes.append([titulo,preco,link_encurtado])

	for i in volumes:
		print (i[0])
		print (i[1])
		print (i[2])
		print()

	return volumes