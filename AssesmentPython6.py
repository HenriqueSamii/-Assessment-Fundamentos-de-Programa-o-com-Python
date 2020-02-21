#Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista
#contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.
tulpeOriginal = (1,2,3,4,5,6,7,8,9,10)
holderPar = ()
holderImpar = []

for item in tulpeOriginal:
    if item%2 == 0:
        holderPar = holderPar + (item,)
    else:
        holderImpar.append(item)

print(holderPar)
print(holderImpar)