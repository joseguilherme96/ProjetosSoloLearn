import sys

# Adiciona o caminho dos módulos na variavel do sistema
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

produtos_pesquisados = [
    'Arroz',
    'Feijão','Feijao',
    'Acucar','Açucar','Adoçante','Xilitol','Pack',
    'Agua','Água'
]

for x in range(len(links_das_paginas)):

    # Requisitando pagina html de produtos de um determinado supermercado
    html_doc = requests.get(links_das_paginas[x])

    soup = BeautifulSoup(html_doc.content,"html5lib")

    # Exibe código da pagina
    #print(soup.prettify())

    lista_produtos = []

    # Adiciona produtos a lista
    for link in soup.find_all('a'):
        nome = link.get("aria-label")
        if(link.get("aria-label") != None):
            for produto in produtos_pesquisados:
                    end = len(produto)
                    if(nome[0:end] == produto or nome[0:end] == produto):
                        lista_produtos.append(link.get("aria-label"))

    lista_precos = []

    # Adiciona preço dos produtos a lista
    for area_produto in soup.find_all('div'):
        lista_classes_tag = area_produto.get("class")
        if(lista_classes_tag != None and len(lista_classes_tag) > 0):
            if(lista_classes_tag[0]=="area-preco"):
                valor = area_produto.div.contents[1]
                lista_precos.append(valor)

    lista_produtos[:]= numpy.unique(lista_produtos)

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