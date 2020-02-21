#Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
#O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.
holder = 0
geter = int(input("Número - "))
for items in range(0,geter+1,2):
    #print(items)
    holder += items
    
print(holder)