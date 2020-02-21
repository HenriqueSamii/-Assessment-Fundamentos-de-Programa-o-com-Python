#Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, 
# e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. 
# Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.
numero = int(input("Número - "))
elevado = int(input("Elevado a - "))

def potencia(A,B):
    holder = 1

    for items in range(B):
        holder *= A
    
    return holder
    
#print(potencia(2,5))
print(potencia(numero,elevado))