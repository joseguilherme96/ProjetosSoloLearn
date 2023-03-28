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

    lista_produtos = []

    # Adiciona produtos a lista
    products_area  = soup.find('div',{'class':'products-area'}).find_all('a');

    for produto in products_area:
        if(len(produto.get('aria-label')) > 5 and produto.get('aria-label') not in lista_produtos):
            lista_produtos.append(produto.get('aria-label'))


    lista_precos = []

    # Adiciona preço dos produtos a lista
    for produto in products_area:
        preco = produto.div

        if(produto.get('aria-label') in lista_produtos and preco != None and preco.get('class')[0] == 'area-bloco-preco'):
            lista_precos.append(preco.contents[1])


    #lista_pro'dutos[:]= numpy.unique(lista_produtos)

    print("Exibindo produtos do site")

    for x in range(len(lista_produtos)):

        produto = lista_produtos[x];
        preco = lista_precos[x];

        print(produto,preco)

    # Teste
    # A Quantidade de produtos armazenado na lista tem que ser igual a quantidade de preço armazenado na lista
    print("\n Teste")
    teste = len(lista_produtos) == len(lista_precos)

    print("Resultado ------> Esperado")
    print(len(lista_produtos) == len(lista_precos), "----->>> True")

    if(teste == False):
        print("Nem todos os produtos do site foram exibidos !!!")
