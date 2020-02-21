#Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
#https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
#E:
#A. Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
#Curling
#Patinação no gelo (skating)
#Esqui (skiing)
#Hóquei sobre o gelo (ice hockey)
#B. Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. 
# Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

import urllib3, requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"

csv = requests.get(url).text

linhas = csv.splitlines()

colunas = linhas[0].split(",")

array = []

for linha in linhas:
    dicionario = {}
    dados = linha.split(",")
    i = 0
    for coluna in colunas:
        dicionario[coluna] = dados[i]
        i += 1
    array.append(dicionario)

del array[0]

##### Testar Biblioteca ########
"""for i in array:
    if  i["NOC"] == "DEN":
        print(i["NOC"])"""
#print(array)
################################

#### A. ########################

# "NOR" "SWE" "DEN"
ouroNOR = 0
ouroSWE = 0
ouroDEN = 0

"""for  i in array:
    if (int(i["Year"]) >= 2001) and (i["Medal"] == "Gold") and (i["Event"] == "skating" or i["Event"] == "skiing" or i["Event"] == "ice hockey"or i["Event"] == "Curling"):
        if  i["NOC"] == "NOR":
            ouroNOR += 1
        if  i["NOC"] == "SWE":
            ouroSWE += 1
        if  i["NOC"] == "DEN":
            ouroDEN += 1"""

for  i in array:
    if (int(i["Year"]) >= 2001) and (i["Medal"] == "Gold") and (i["Sport"] == "Skating" or i["Sport"] == "Skiing" or i["Sport"] == "Ice Hockey"or i["Sport"] == "Curling"):
        if  i["NOC"] == "NOR":
            ouroNOR += 1
        if  i["NOC"] == "SWE":
            ouroSWE += 1
        if  i["NOC"] == "DEN":
            ouroDEN += 1
        
#print(ouroNOR)
#print(ouroSWE)
#print(ouroDEN)

maiorMedalista = "Erro, nenum deles teve ouro ou teve empate entre dois ou mais países"

if ouroNOR>ouroSWE and ouroNOR>ouroDEN:
    maiorMedalista = "Noruega"
elif ouroSWE>ouroNOR and ouroSWE>ouroDEN:
    maiorMedalista = "Suécia"
elif ouroDEN>ouroNOR and ouroDEN>ouroSWE:
    maiorMedalista = "Dinamarca"

print("A.\nNo século XXI o maior medalhista de ouro é - "+maiorMedalista)

################################
#### B. ########################

#B. Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. 
# Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

arrayRespostaB = []
paisExisteEmArrayB = False

for  i in array:
    for grupos in arrayRespostaB:
        if i["NOC"]==grupos["Pais"]:
            paisExisteEmArrayB = True
    if paisExisteEmArrayB == False:
        gruposPaises = {"Pais":i["NOC"],"Detalhes":[]}
        arrayRespostaB.append(gruposPaises)
    
    for j in range(len(arrayRespostaB)):
        if arrayRespostaB[j]["Pais"] == i["NOC"]:

            medalha = i["Medal"]
            genero = ""

            if medalha == "Gold":
                medalha = "Ouro"
            elif medalha == "Silver":
                medalha = "Prata"

            if i["Event gender"] == "M":
                genero = "Masculino"
            elif i["Event gender"] == "W":
                genero = "Feminino"

            detalhesLibrary = {"Medalha":medalha,"Esport":i["Sport"],"Ano":i["Year"],"Cidade":i["City"],"Genero":genero}
            arrayRespostaB[j]["Detalhes"].append(detalhesLibrary)

    paisExisteEmArrayB = False

for respostaFinalB in arrayRespostaB:
    print("\n\nPais "+ respostaFinalB["Pais"] + " tem "+ str(len( respostaFinalB["Detalhes"])) +" medalhas")
    print("Quer foram de:")
    for detalhe in  respostaFinalB["Detalhes"]:
        print(detalhe["Medalha"] + ", no esporte " + detalhe["Esport"]+ " em " + detalhe["Ano"] + ", na cidade " + detalhe["Cidade"] + ", no gênero " + detalhe["Genero"])

################################