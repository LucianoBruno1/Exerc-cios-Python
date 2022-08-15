##faça um script que mostre a tabuada de um número indeterminado de numeros

cont = 0

while True:
    x = int(input('Digite um número inteiro para saber sua tabuada: '))

    if x < 0:
        print('Reinicie o programa e digite um número positivo válido.')
        break

    while cont < 9:
        cont+=1
        print('{} * {} = {}'.format(x,cont, x * cont))


        if cont == 9:
            cont = 0
            break
