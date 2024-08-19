from bs4 import BeautifulSoup as soup
import pyshorteners

def PesquisarDados ():
	print ("\nMÓDULO 2------------------------------------------------------------------------\n")
	#construindo um objeto Beautiful Soup
	endereco = open ("C:/Users/erick/Documents/codes/Amazon_Vigiar_Preco/local_soup_html.html", "r", encoding = "utf-8")
	site = endereco.read()
	local_soup = soup(site, 'html.parser')	

	#fazendo pesquisas
	titulos = local_soup.find_all ("span", class_= "a-size-base-plus")
	precos = local_soup.find_all ("span", class_= "a-price-whole")
	print (f"Tamanho original precos: {len(precos)}")
	print (precos [16])

	links = local_soup.find_all ("a", class_= "a-link-normal s-no-outline")
	links = [i["href"] for i in links]
	links = ["https://www.amazon.com.br"+i for i in links]

	#adicionar na lista
	lista_titulos = []
	lista_precos = []
	lista_links = []

	x = 0
	for l in titulos:
		if 'ONE PIECE 3 EM 1' in titulos[x].get_text().upper() or 'ONE PIECE (3 EM 1)' in titulos[x].get_text().upper():
			lista_titulos.append (titulos[x].get_text().strip())
			#if 'R$' in precos [x].get_text():
			lista_precos.append (int (precos[x].get_text().replace("\n", "").replace ("'","").replace (",","").strip()))
			lista_links.append (links[x])
		x += 1

	#transformar preco string para float
	#lista_precos_float = [float(i[3:].replace(",",".")) for i in lista_precos]

	#encurtar o link
	encurtador = pyshorteners.Shortener()
	lista_links = [encurtador.tinyurl.short(i) for i in lista_links]

	#imprimir valores
	print (f"\nTamanho: {len(lista_titulos)}")
	print (lista_titulos)
	print (f"\nTamanho: {len(lista_precos)}")
	#print (lista_precos)
	print (lista_precos)
	print (f"\nTamanho: {len(lista_links)}")
	print (lista_links)
	
	#retornar valores
	valores = [lista_titulos, lista_precos, lista_links]
	return valores