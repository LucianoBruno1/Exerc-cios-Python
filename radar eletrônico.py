from time import sleep
print('\nBem vindo à página do DETRAN-PE. Você foi notificado sobre uma multa.\n\n')

velocidade = int(input('Digite a velocidade do carro no momento em que passou no radar: '))
print('PROCESSANDO...')
sleep(2)

multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado em: R${} '.format(multa))
else:
    print('Você está dentro do limite permitido.')