'''
Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada.
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).
'''

lista=[]
palpite = 0

while type(palpite) == int and palpite >= 0:
    palpite = int(input('Indique um número inteiro positivo: '))
    if palpite >= 0:
        lista.append(palpite)
    else:
        break

print(lista)