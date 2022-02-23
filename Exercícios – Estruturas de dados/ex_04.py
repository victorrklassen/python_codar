'''
Suponha o seguinte programa

# Alunos e suas respectivas notas
alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

Escreva uma programa que calcula a média das notas de todos os alunos
'''

alunos = [
("Alice", 8),
("Bob", 7),
("Carlos", 9),
]

soma = 0
for aluno in alunos:
    soma += alunos[0][1]
    media = soma/len(alunos)

print(soma)
print(media)