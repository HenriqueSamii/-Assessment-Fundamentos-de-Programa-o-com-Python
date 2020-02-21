#Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
# A. Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
# B. Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela.
#  O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

from bs4 import BeautifulSoup
import requests #,urllib3

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')

####### A. #################

array = []
dicsionayTabela = {}

for i in soup.html.body.find('div',{'class':'tabela'}).find('div',{'class':'titulo'}).find_all('div',{'class':'celula'}):
    dicsionayTabela[i.text] = ""

for i in soup.html.body.find('div',{'class':'tabela'}).find_all('div',{'class':'linha'}):
    novoDic = dicsionayTabela.copy()
    arrayDeCelulas = i.find_all('div',{'class':'celula'})
    position = 0
    for x in novoDic:
        novoDic[x] = arrayDeCelulas[position].text
        position += 1
    array.append(novoDic)

#print(array)

for i in array:
    for x, y in i.items():
        print(x + " - " + y)
    print("")
############################

####### B. #################

siglaDoUser = input("Sigla que proucura do estado da região Centro-Oeste - ")

itemProucura = False

for i in array:
    if siglaDoUser == i['Sigla']:
        itemProucura = i

if itemProucura == False:
    print("Essa sigla não pertence à região")
else:
    for x, y in itemProucura.items():
        print(x + " - " + y)


############################