menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    elif peso > maior:
         maior = peso
    elif peso < menor:
         menor = peso



print('O maior peso é: {} e o menor é {}'.format(maior, menor))