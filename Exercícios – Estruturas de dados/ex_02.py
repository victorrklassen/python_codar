'''
Dada uma lista de números inteiros, escreva um programa que calcula a soma de
todos os números na lista.
Se preferir, pode utilizar a lista abaixo como exemplo:

lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100
'''
lista=[]
palpite = 0
soma = 0

while type(palpite) == int and palpite >= 0:
    palpite = int(input('Indique um número inteiro positivo: '))
    if palpite >= 0:
        lista.append(palpite)
        soma += palpite
    else:
        break

print(lista)
print('A soma dos números armazenados é: {}'.format(soma))