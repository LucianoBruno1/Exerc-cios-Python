media = 0
cont = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres = 0
for c in range (1,5):
    cont+=1
    print('-='*20)
    print('{}° PESSOA'.format(cont))
    nome = str(input('Qual seu nome?: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    somaidade+=idade
    media = somaidade / c

    if cont == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        cont = 0
        cont+=1
        mulheres+=cont

print('A média de idade do grupo é: {}'.format(media))
print('O nome do homem mais velho é: {}'.format(nomevelho))
print('A quantidade de mulheres abaixo de 20 anos é: {}'.format(mulheres))