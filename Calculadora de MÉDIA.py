nota1 = float(input(print('Digite sua primeira nota: ')))
nota2 = float(input(print('Digite sua segunda nota: ')))
nota3 = float(input(print('Digite sua terceira nota: ')))
media = (nota1 + nota2 + nota3)/3

if media >=7:
    print('Parabéns, você está aprovado com média: {}'.format(media))
else:
    print('Você está reprovado com média: ', media)