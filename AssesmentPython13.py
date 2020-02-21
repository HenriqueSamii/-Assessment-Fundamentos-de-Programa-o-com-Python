#Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
# A. Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
# B. Conte quantas vezes apareceu a palavra ladies no conteúdo da página

from bs4 import BeautifulSoup
import requests, re #,urllib3

url = "http://brasil.pyladies.com/about"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')

####### A. #################

texto = soup.html.body.find('article',{'class':'notepad-page-content'}).text.lower()
texto = texto.replace("**", "")
texto = texto.replace(".", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")
texto = texto.replace(",", "")

palavrasTextoArray = texto.split()
palavrasDic = {}

for i in palavrasTextoArray:
    if i in palavrasDic:
        palavrasDic[i] += 1
    else:
        palavrasDic[i] = 1

numeroDePalavrasUnicas = 0
quaisPalavrasUnicas = ""

for x,y in palavrasDic.items():
    if y == 1:
        numeroDePalavrasUnicas += 1
        quaisPalavrasUnicas += x+", "

print("Existem " + str(numeroDePalavrasUnicas) + " palavras unicas")
print("E elas são:\n" + quaisPalavrasUnicas.rstrip(', ') + ".")

############################

####### B. #################

#ladiesArray = texto.split("ladies")
#print(len(ladiesArray))

ladiesArray = re.findall("ladies", texto)
print("ladies apareceu " + str(len(ladiesArray)) + " vezes")


############################