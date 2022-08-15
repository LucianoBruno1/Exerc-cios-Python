from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = []
jogo['jogador 1'] = randint(1, 6)
jogo['jogador 2'] = randint(1,6)
jogo['jogador 3'] = randint(1,6)
jogo['jogador 4'] = randint(1,6)

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'O {k} teve o valor de: {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):


    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

