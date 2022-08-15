nome = str(input('Digite seu nome: ')).strip()

print('Seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))

print('Seu nome com todas as letras minúsculas é: {} '.format(nome.lower()))

print('A quantidade de letras do seu nome é: {} '.format(len(nome)-nome.count(' ')))

print('A quantidade de letras do seu primeiro nome é: {}'.format(nome.find(' ')))



