'''
DESAFIO. Escreva um programa que declara uma lista com elementos de
diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
métodos como reverse ou sort .
def inverte_lista(lista):
...
lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)
# [{1}, 5, "a"]
'''

def inverte_lista(lista):
    invertida =[]
    posicao = len(lista)-1
    while posicao >= 0:
        invertida.append(lista[posicao])
        posicao -= 1
    return invertida

lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)