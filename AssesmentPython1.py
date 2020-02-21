#Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.
tupleO = (15,10,11)

def invert_items():
    global tupleO
    arrayHolder = []
    arrayHolder.append(tupleO[0])
    for items in range(len(tupleO)):
        posision = 0
        while tupleO[items] > arrayHolder[posision] and posision < len(tupleO) :
            posision += 1
        arrayHolder.insert( posision, tupleO[items])
    arrayHolder.remove(tupleO[0])
    tupleO = tuple(arrayHolder)

invert_items()
    
print(tupleO)