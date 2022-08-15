num1 = int(input('Digite o número 1:'))
num2 = int(input('Digite o número 2: '))

cont = num1
soma = 0
mult = 1

while cont<= num2:
    cont+=1
    if cont% 2 == 0:
        print('par = {}'.format(cont))
        soma =+cont
    else:
        mult = mult*cont

    print('Soma é {}'.format(soma))
    print('Multiplicação é {}'.format(mult))