from random import randint #randint é o comando da biblioteca random para sortear
from time import sleep #sleep é o comando da biblioteca time para dar um tempo entre comandos
computador = randint(0, 5)


print('-=-' *20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
print('-=-' *20)



jogador = int(input('Digite o número em que você acha que o computador está pensando: '))
print('PROCESSANDO....')
sleep(3)
if jogador == computador:
    print('PARABÉNS! VOCÊ ACERTOU.')
else:
    print('Você errou. O computador pensou no número {}'.format(computador))