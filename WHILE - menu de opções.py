from time import sleep
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))


escolha = 0
while escolha != 5:
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] para maior')
    print('[4] para novos numeros')
    print('[5] para sair do programa')

    escolha = int(input('Digite um valor de 1 a 4 para as operações ou sair para fechar o programa: '))

    if escolha == 1:
        soma = num1 + num2
        print('a soma de {} + {} é igual a: {}\n'.format(num1, num2, soma))
        sleep(2)

    elif escolha == 2:
        mult = num1 * num2
        print('A multiplicação de {} * {} é igual a: {}\n'.format(num1,num2,mult))
        sleep(2)
    elif escolha == 3:
        if num1 > num2:
            print('{} é maior que {}\n'.format(num1, num2))
            sleep(2)
        if num2 > num1:
            print('{} é maior que {}\n'.format(num2, num1))
            sleep(2)

    elif escolha == 4:
        num1 = int(input('Digite um novo numero : '))
        num2 = int(input('Digite outro novo numero: '))

    elif escolha == 5:

      print('Obrigado por utilizar o programa!\n')
      break

    else:
        print('opção inválida, tente novamente\n.')
    print('=-=' * 10)








