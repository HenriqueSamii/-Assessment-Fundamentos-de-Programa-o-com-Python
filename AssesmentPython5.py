#Usando a biblioteca ‘turtle’ crie uma função que desenhe a imagem a seguir:
import turtle,math

# Coverção de n de quadrado para circulo e contrario #

#raioCurculo = 360*n/(2*math.pi)
#nDeCirculo = (2*math.pi*(nDeQuadrado/2))/360

def n_de_circulo(nDeQuadrado):
    return (2*math.pi*(nDeQuadrado/2))/360

def n_de_quadrado(nDeCirculo):
    return 360*nDeCirculo/(2*math.pi)

######################################################

####### Funções criar quadrado e circulo #############

def quadrado(n):
    for target_list in range(4):
        turtle.forward(n)
        turtle.left(90)

def circulo(n):
    for target_list in range(360):
        turtle.forward(n)
        turtle.left(1)

######################################################

####### Função criar imagem a seguir #################

def imagem_a_seguir (n):
    y=300

    #while n-y>0:
    for target_list in range(n):
        tamanhoMuldura = y
        tamanhoItensEmMuldura = tamanhoMuldura*0.4
        ceparacaoItens = tamanhoMuldura*0.1
        padding = tamanhoMuldura*0.05
        ### Quadrado Muldura ##########
        quadrado(tamanhoMuldura)
        ###############################
        ### Mover dentro da Muldura ###
        turtle.pu()
        turtle.left(90)
        turtle.forward(padding)
        turtle.right(90)
        turtle.forward(padding)
        turtle.pd()
        ###############################
        ### Desenhar item em Muldura ##
        quadrado(tamanhoItensEmMuldura)
        turtle.pu()
        turtle.forward(tamanhoItensEmMuldura+ceparacaoItens+(tamanhoItensEmMuldura/2))
        turtle.pd()
        circulo(n_de_circulo(tamanhoItensEmMuldura))
        turtle.pu()
        turtle.left(90)
        turtle.forward(tamanhoItensEmMuldura+ceparacaoItens)
        turtle.right(90)
        turtle.pd()
        circulo(n_de_circulo(tamanhoItensEmMuldura))
        turtle.pu()
        turtle.back(tamanhoItensEmMuldura+ceparacaoItens+(tamanhoItensEmMuldura/2))
        turtle.pd()
        quadrado(tamanhoItensEmMuldura)
        turtle.pu()
        turtle.right(90)
        turtle.forward(tamanhoItensEmMuldura+ceparacaoItens)
        turtle.left(90)
        turtle.pd()
        ###############################
        y = tamanhoItensEmMuldura

######################################################

#circulo(0.5)
#quadrado(((360*0.5)/(2*math.pi))*2)

#quadrado(100)
#circulo((2*math.pi*(100/2))/360)
        
imagem_a_seguir(5)

input("Enter para terminar programa")