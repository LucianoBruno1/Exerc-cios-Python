num = int(input('Digite um número para saber seu fatorial: '))

cont = num
soma = 0
while cont > 2:

    cont-=1
    num*=cont
    soma+=num
    print('{}'.format(num))





