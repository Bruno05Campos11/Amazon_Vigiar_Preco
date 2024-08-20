from bs4 import BeautifulSoup as soup
import pyshorteners

def PesquisarDados ():
	print ("\nMÓDULO 2------------------------------------------------------------------------\n")
	#construindo um objeto Beautiful Soup
	endereco = open ("C:/Users/erick/Documents/codes/Amazon_Vigiar_Preco/local_soup_html.html", "r", encoding = "utf-8")
	site = endereco.read()
	local_soup = soup(site, 'html.parser')	

	#fazendo pesquisas
	volumes = []

	cards = local_soup.find_all ("div", class_="puis-card-container")
	for card in cards:
		titulo = card.find ("span", class_= "a-size-base-plus").get_text().strip()
		preco = card.find ("span", class_= "a-price-whole")
		if preco != None:
			preco = int (preco.get_text().replace(",","").strip())
		else:
			preco = int()
		link = card.find ("a", class_= "a-link-normal s-no-outline")
		link = "https://www.amazon.com.br" + link["href"]
		link_encurtado = pyshorteners.Shortener().tinyurl.short (link)

		if 'ONE PIECE 3 EM 1' in titulo.upper() or 'ONE PIECE (3 EM 1)' in titulo.upper():
			volumes.append([titulo,preco,link_encurtado])

	for i in volumes:
		print (i[0])
		print (i[1])
		print (i[2])
		print()


	#transformar preco string para float
	#lista_precos_float = [float(i[3:].replace(",",".")) for i in lista_precos]

	return volumes