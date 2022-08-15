print(' \nNotas para o curso de Sistemas de Informação\n ')


humanas = float(input('Digite sua nota de humanas: '))
naturezas = float(input('Digite sua nota de Naturezas: '))
linguagens = float (input('Digite sua nota de linguagens: '))
matematica = float(input('Digite sua nota de Matemática: '))
redacao = int(input('Digite sua nota de redação: '))

pesomatematica = matematica * 4
pesoredacao = redacao * 3

media = (humanas + naturezas + linguagens + pesomatematica + pesoredacao) / 10

if media >= 780:
    print('\nPARABÉNS! você foi aprovado com nota {} para o curso de Sistemas de Informação!'.format(media))
else:
    print('\nVocê não atingiu a nota minima necessária. Sua nota foi : {}'.format(media))

