import sys

# Adiciona o caminho dos módulos na variavel do sistema que salva o caminho dos módulos
sys.path.append("c:\\users\\josé guilherme\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")

from bs4 import BeautifulSoup
import requests
import numpy

links_das_paginas = [
    'https://www.sitemercado.com.br/mairinquesupermercado/mairinque-loja-monteiro-lobato-centro-rua-monteiro-lobato/produtos/alimentos-basicos/arroz',
    'https://www.sitemercado.com.br/mairinquesupermercado/mairinque-loja-monteiro-lobato-centro-rua-monteiro-lobato/produtos/alimentos-basicos/feijao',
    'https://www.sitemercado.com.br/mairinquesupermercado/mairinque-loja-monteiro-lobato-centro-rua-monteiro-lobato/produtos/alimentos-basicos/acucares-e-adocantes',
    'https://www.sitemercado.com.br/mairinquesupermercado/mairinque-loja-monteiro-lobato-centro-rua-monteiro-lobato/produtos/bebidas/aguas'
]

for x in range(len(links_das_paginas)):

    # Requisitando pagina html de produtos de um determinado supermercado
    html_doc = requests.get(links_das_paginas[x])

    soup = BeautifulSoup(html_doc.content,"html5lib")

    # Exibe código da pagina
    #print(soup.prettify())

    dicionario = {}

    # Adiciona produtos a lista
    products_area  = soup.find('div',{'class':'products-area'}).find_all('a');

    x= 0
    for produto in products_area:
        preco = produto.div
        nomeProduto = produto.get('aria-label')

        if(len(nomeProduto) > 5 and nomeProduto not in dicionario and preco != None and \
        preco.get('class')[0] == 'area-bloco-preco'):
        
            if nomeProduto.lower().find("kg") != -1:
                end = nomeProduto.lower().find("kg") # Encontra unidade peso
                start = end - 1
                end = end + 2
                peso = nomeProduto[start:end]

            elif nomeProduto.lower().find("ml") != -1:
                end = nomeProduto.lower().find("ml")  # Encontra unidade ml
                start = end - 1
                try:
                    while int(nomeProduto[start:end]) >=0:
                        start-=1
                except:
                    start+=1
                    end = end + 2
                    peso = nomeProduto[start:end].strip()
            else:
                peso = nomeProduto[start:end]
                peso= None

            dicionario[x] = {
                'nomeProduto : ':produto.get('aria-label'),
                'precoProduto :': preco.contents[1],
                'tamanho':peso}
            x+=1

    print("Exibindo produtos do site")

    for produtos in dicionario.items():
        print(produtos)