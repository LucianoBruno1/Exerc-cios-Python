
opcao = 0
soma = subtraçao = 0
mult = 1
div = 1
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um segundo número: '))

while opcao !=5:
    print(' [1] SOMA \n [2] SUBTRAÇÃO\n [3] MULTIPLICAÇÃO\n [4] DIVISÃO\n [5] SAIR DO PROGRAMA')
    opcao = int(input('Digite o número da opção que deseja realizar a operação: '))

    if opcao == 1:
        soma = num1+num2
        print('A soma é: {}'.format(soma))

    elif opcao == 2:
        subtraçao = num1 - num2
        print('A subtração é: {}'.format(subtraçao))

    elif opcao == 3:
        mult = num1 * num2
        print('A multiplicação é: {}'.format(mult))

    elif opcao == 4:
        div = num1/num2
        print('A divisão é: {}'.format(div))

    elif opcao == 5:
        print('Programa encerrado.')
        break

    else:
        print('Digite um número válido')
        continue






