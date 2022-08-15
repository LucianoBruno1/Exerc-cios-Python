frase = str(input('Digite uma frase: ')).lower().strip()

print('A letra ''A'' aparece {} vezes na frase'.format(frase.count('a')))
print('A letra ''A'' aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A última posição em que a letra "A" aparece é na posição {}'.format(frase.rfind('a')+1))
