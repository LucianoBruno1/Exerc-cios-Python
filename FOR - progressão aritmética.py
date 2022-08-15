num = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão: '))
soma = 0
for c in range(1,11):
    num+=razao
    print('{} -> '.format(num),end='')