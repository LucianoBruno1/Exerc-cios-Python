from random import randint

computador = randint(0,10)
print('Vou pensar em um número entre 0 e 10, tente adivinhar!')
palpites = 0
jogador = 0

while jogador != computador:
    jogador = int(input('Digite o número que acha que estou pensando: '))
    palpites += 1
    if jogador == computador:
        print('ACERTOU! você teve {} tentativas.'.format(palpites))
    elif jogador > computador:
        print('menos..')
    elif jogador < computador:
        print('mais...')

