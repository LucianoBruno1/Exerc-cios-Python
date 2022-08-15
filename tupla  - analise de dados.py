num = (int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')),
       int(input('Digite um número inteiro: ')))

print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 está na posição: {num.index(3)}')
else:
    print('O valor 3 não está na sequencia.')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n %2 == 0:
        print(n, end=' ')