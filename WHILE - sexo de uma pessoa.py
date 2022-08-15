
sexo = str(input('Digite seu sexo: [F/M]: ')).strip().upper()
while sexo not in 'MmfF':
    sexo = str(input('Dados inválidos, por favor, informe seu sexo: ')).strip().upper()[0]

print('Seu sexo é {}'.format(sexo))



