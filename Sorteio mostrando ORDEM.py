from random import shuffle
n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digte o nome do aluno 4: ')

lista = [n1,n2,n3,n4]
shuffle(lista)

print('A ordem de apresentação do trabalho é: ')
print(lista)