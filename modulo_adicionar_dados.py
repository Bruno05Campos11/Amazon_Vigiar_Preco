from bs4 import BeautifulSoup as soup

def PesquisarDados ():
	print ("\nMÓDULO 2------------------------------------------------------------------------\n")
	#construindo um objeto Beautiful Soup
	endereco = open ("C:/Users/erick/Documents/codes/Amazon_Vigiar_Preco/local_soup_html.html", "r", encoding = "utf-8")
	site = endereco.read()
	local_soup = soup(site, 'html.parser')	

	#fazendo pesquisas
	titulos = local_soup.find_all ("span", class_= "a-size-base-plus")
	precos = local_soup.find_all ("span", class_= "a-offscreen")
	'''link = item.find ("a", class_= "").get_text()'''

	#adicionar na lista
	lista_titulos = []
	lista_precos = []
	x = 0
	for l in titulos:
		if 'ONE PIECE 3 EM 1' in titulos[x].get_text().upper() or 'ONE PIECE (3 EM 1)' in titulos[x].get_text().upper():
			lista_titulos.append (titulos[x].get_text().strip ())
			lista_precos.append (titulos[x].get_text().strip())
		x += 1

	#retornar valores
	valores = [lista_titulos, lista_precos]
	return valores