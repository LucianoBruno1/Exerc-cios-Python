#ex002: faça um programa que mostre o nome de uma pessoa e uma mensagem de boas vindas.

gasolina = float(input('Digite o preço da gaoslina:  '))
alcool = float(input('Digite o preço do alcool:  '))

if alcool <= 0.7 * gasolina:
    print(' Abasteça com alcool')
else: print('abasteça com gasolina')