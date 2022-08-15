
distancia = int(input('\nDigite a distância da viagem que você deseja fazer (em km): '))
preço = 0

if distancia <=200:
    preço = distancia * 0.5
    print('A passagem custa: R${}'.format(preço))
else:
    preço = 0.45 * distancia
    print('A passagem para essa distância custa: R${}'.format(preço))