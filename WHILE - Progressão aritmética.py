#Faça um código que mostre a progreção aritmética lendo o primeiro termo
#e a razão de uma P.A mostrando os 10 primeiros termos da P.A. com WHILE



cont = 1
primeirotermo = int(input('\nDigie um número para saber sua P.A: '))
razao = int(input('\nDigite a razão da P.A: '))

while cont < 10:
        cont += 1
        primeirotermo += razao
        print('{} -> '.format(primeirotermo), end='')
print('FIM')





