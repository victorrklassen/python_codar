'''
Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12
'''

lista=[]
palpite = 0
soma = 0

while type(palpite) == int and palpite >= 0:
    palpite = int(input('Indique um número inteiro positivo: '))
    if palpite >= 0:
        lista.append(palpite)
        soma += palpite
        media = soma/len(lista)
    else:
        break

print(lista)
print('A média dos números armazenados é: {}'.format(int(media)))