'''
DESAFIO. Uma string ( str ) também pode ser percorrida utilizando o for .

for x in "abc":
print(x)
# Vai imprimir:
# a
# b
# c

Escreva um programa que solicite uma string para o usuário e imprima quantas
vezes cada letra aparece na palavra. 

Por exemplo:
"banana"
# O resultado deve ser
{
'a': 3,
'b': 1,
}
'''

texto = input('Insira uma palavra: ')

alpha=[]
b_count = []
#print(b_count)

for i in texto:
    alpha.append(i)

betha = list(set(alpha))
#print(betha)

for b in betha:
        b_count.append(0)

#print(b_count)

k = int(len(betha))-1
m = 0

for b in betha:
    for i in texto:
        if i == b:
#            print('{} é igual à {}'.format(i,b))
            b_count[m] += 1
#            print(b_count)
        else:
            False
#            print('{} não é igual à {}'.format(i,b))
    m +=1

print(betha)
print(b_count)