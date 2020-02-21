#Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
#a. Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
#b. Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
#c. Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
#d. Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.

import urllib3, requests

url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv"

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

#### Genre e Publishers (marca) array ###################################

arrayPublishers = []
publisherExisteEmArrayPublishers = False
anoRecent = 2016

for i in array:
    #if i["Year_of_Release"] != "N/A" and int(i["Year_of_Release"]) > anoRecent:
    #    anoRecent = int(i["Year_of_Release"])
    if i["Genre"] == "Action" or i["Genre"] == "Shooter" or i["Genre"] == "Platform":
        for publisher in arrayPublishers:
            if i["Publisher"]==publisher["Nome"]:
                publisherExisteEmArrayPublishers = True
        if publisherExisteEmArrayPublishers == False:
            pupliserCompleto = {"Nome":i["Publisher"],"Detalhes":[]}
            arrayPublishers.append(pupliserCompleto)
        
        for j in range(len(arrayPublishers)):
            if arrayPublishers[j]["Nome"] == i["Publisher"]:
                detalhesLibrary = {"Genero":i["Genre"],"Ano":i["Year_of_Release"],"VendasGlobal":i["Global_Sales"],"VendasJapao":i["JP_Sales"]}
                arrayPublishers[j]["Detalhes"].append(detalhesLibrary)

        publisherExisteEmArrayPublishers = False

"""for target_list in arrayPublishers:
    if target_list["Nome"]=="Microsoft Game Studios":
        print(target_list)"""

########################################################################

#### A. ########################
#a. Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.

maisPuplicacoes = [{"Nome":"","Detalhes":[]},{"Nome":"","Detalhes":[]},{"Nome":"","Detalhes":[]}]

for i in arrayPublishers:
    if len(i["Detalhes"])> len(maisPuplicacoes[0]["Detalhes"]):
        maisPuplicacoes[2] = maisPuplicacoes[1]
        maisPuplicacoes[1] = maisPuplicacoes[0]
        maisPuplicacoes[0] = i
    elif len(i["Detalhes"])> len(maisPuplicacoes[1]["Detalhes"]):
        maisPuplicacoes[2] = maisPuplicacoes[1]
        maisPuplicacoes[1] = i
    elif len(i["Detalhes"])> len(maisPuplicacoes[2]["Detalhes"]):
        maisPuplicacoes[2] = i

print("As três marcas que mais publicaram jogos dos três gêneros combinados foram:")
for i in maisPuplicacoes:
    print(" - "+i["Nome"]+" com "+str(len(i["Detalhes"]))+" jogos publicados")

################################

#### B. ########################
#b. Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.

maisVendidas = [[{"Nome":"","Detalhes":[]},0],[{"Nome":"","Detalhes":[]},0],[{"Nome":"","Detalhes":[]},0]]

for i in arrayPublishers:
    holderVendas = 0
    for j in i["Detalhes"]:
        holderVendas += float(j["VendasGlobal"])
    if holderVendas > maisVendidas[0][1]:
        maisVendidas[2] = maisVendidas[1]
        maisVendidas[1] = maisVendidas[0]
        maisVendidas[0] = i,holderVendas
    elif holderVendas > maisVendidas[1][1]:
        maisVendidas[2] = maisVendidas[1]
        maisVendidas[1] = i,holderVendas
    elif holderVendas > maisVendidas[2][1]:
        maisVendidas[2] = i,holderVendas

print("\nAs três marcas que mais venderam jogos dos três gêneros combinados foram:")
for i in maisVendidas:
    print(" - "+i[0]["Nome"]+" com "+str(i[1])+" jogos vendidos")

################################

#### C. ########################
#c. Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela. ação (Action), tiro (Shooter) e plataforma (Platform)

maisPublicacoesJapAction = [{"Nome":"","Detalhes":[]},0]
maisPublicacoesJapShooter = [{"Nome":"","Detalhes":[]},0]
maisPublicacoesJapPlatform = [{"Nome":"","Detalhes":[]},0]

for i in arrayPublishers:
    holderJapAction = 0
    holderJapShooter = 0
    holderJapPlatform = 0
    for j in i["Detalhes"]:
        if j["Ano"] != "N/A" and int(j["Ano"]) >= anoRecent-10:
            if j["Genero"] == "Action":
                holderJapAction += 1
            elif j["Genero"] == "Shooter":
                holderJapShooter += 1
            elif j["Genero"] == "Platform":
                holderJapPlatform += 1
    if holderJapAction > maisPublicacoesJapAction[1]:
        maisPublicacoesJapAction = i,holderJapAction
    elif holderJapShooter > maisPublicacoesJapShooter[1]:
        maisPublicacoesJapShooter = i,holderJapShooter
    elif holderJapPlatform > maisPublicacoesJapPlatform[1]:
        maisPublicacoesJapPlatform = i,holderJapPlatform

print("\nAs três marcas com mais publicações em cada um dos gêneros nos últimos dez anos no Japão foram:")
print(" - Genero Ação - "+maisPublicacoesJapAction[0]["Nome"]+" com "+str(maisPublicacoesJapAction[1])+" jogos publicados")
print(" - Genero Tiro - "+maisPublicacoesJapShooter[0]["Nome"]+" com "+str(maisPublicacoesJapShooter[1])+" jogos publicados")
print(" - Genero Plataforma - "+maisPublicacoesJapPlatform[0]["Nome"]+" com "+str(maisPublicacoesJapPlatform[1])+" jogos publicados")

################################

#### D. ########################
#d. Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.

"""maisVendasJapAction = [{"Nome":"","Detalhes":[]},0," - Genero Ação - "]
maisVendasJapShooter = [{"Nome":"","Detalhes":[]},0," - Genero Tiro - "]
maisVendasJapPlatform = [{"Nome":"","Detalhes":[]},0," - Genero Plataforma - "]"""

maisVendasJapAction = [{"Nome":"","Detalhes":[]},0]
maisVendasJapShooter = [{"Nome":"","Detalhes":[]},0]
maisVendasJapPlatform = [{"Nome":"","Detalhes":[]},0]

for i in arrayPublishers:
    holderJapAction = 0
    holderJapShooter = 0
    holderJapPlatform = 0
    for j in i["Detalhes"]:
        if j["Ano"] != "N/A" and int(j["Ano"]) >= anoRecent-10:
            if j["Genero"] == "Action":
                holderJapAction += float(j["VendasJapao"])
            elif j["Genero"] == "Shooter":
                holderJapShooter += float(j["VendasJapao"])
            elif j["Genero"] == "Platform":
                holderJapPlatform += float(j["VendasJapao"])
    if holderJapAction > maisVendasJapAction[1]:
        maisVendasJapAction = i,holderJapAction
    elif holderJapShooter > maisVendasJapShooter[1]:
        maisVendasJapShooter = i,holderJapShooter
    elif holderJapPlatform > maisVendasJapPlatform[1]:
        maisVendasJapPlatform = i,holderJapPlatform

print("\nAs três marcas que mais vendeu em cada um desses gêneros nos últimos dez anos no Japão foram:")
print(" - Genero Ação - "+maisVendasJapAction[0]["Nome"]+" com "+str(maisVendasJapAction[1])+" jogos vendidos")
print(" - Genero Tiro - "+maisVendasJapShooter[0]["Nome"]+" com "+str(maisVendasJapShooter[1])+" jogos vendidos")
print(" - Genero Plataforma - "+maisVendasJapPlatform[0]["Nome"]+" com "+str(maisVendasJapPlatform[1])+" jogos vendidos")


"""arrayTodasVendasJap = [maisVendasJapAction,maisVendasJapShooter,maisVendasJapPlatform]
for i in arrayTodasVendasJap:
    print(i[2]+i[0]["Nome"]+" com "+str(i[1])+" jogos vendidos")"""

################################






"""#### Array de Genre: Action, Shooter e Platform ########################

arrayGenre = []

for i in array:
    if i["Genre"] == "Action" or i["Genre"] == "Shooter" or i["Genre"] == "Platform":
        arrayGenre.append(i)

########################################################################

#### arrayPublishers (marca) ###########################################

arrayPublishers = []
publisherExisteEmArrayPublishers = False

for  i in arrayGenre:
    for publisher in arrayPublishers:
        if i["Publisher"]==publisher["Nome"]:
            publisherExisteEmArrayPublishers = True
    if publisherExisteEmArrayPublishers == False:
        pupliserCompleto = {"Nome":i["Publisher"],"Detalhes":[]}
        arrayPublishers.append(pupliserCompleto)
    
    for j in range(len(arrayPublishers)):
        if arrayPublishers[j]["Nome"] == i["Publisher"]:
            detalhesLibrary = {"Genero":i["Genre"],"Ano":i["Year_of_Release"],"VendaGlobal":i["Global_Sales"],"VendasJapao":i["JP_Sales"]}
            arrayPublishers[j]["Detalhes"].append(detalhesLibrary)

    publisherExisteEmArrayPublishers = False


########################################################################"""