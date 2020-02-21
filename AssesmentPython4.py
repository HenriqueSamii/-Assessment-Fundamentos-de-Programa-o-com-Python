#Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas.
#Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].
vector = [4, 3, 5, 1, 2]

for n in range(len(vector)-1):
    vector.insert( n, vector[len(vector)-1])
    vector.pop(len(vector)-1)

print(vector)