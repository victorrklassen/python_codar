'''
DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
o maior número dessa lista.
'''

lista=[]
palpite = 0
soma = 0

while type(palpite) == int and palpite >= 0:
    palpite = int(input('Indique um número inteiro positivo: '))
    if palpite >= 0:
        lista.append(palpite)
        lista.sort()
        n = len(lista)-1

    else:
        break

#print(lista)
print(lista[n])