from math import sqrt
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

operacao = input('Qual operação deseja realizar? (responda com + , - , *, / ):    ')

if operacao == '+':
    print(num1 + num2)

elif operacao == '-' :
    print(num1 - num2)

elif operacao == '*' :
    print(num1 * num2)

elif operacao == '/' :
    print(num1 / num2)

else: print('Você digitou uma operação inválida.')