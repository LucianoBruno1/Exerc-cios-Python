

media = soma = quantidade = maior = menor = mediapar = 0
opcao = 's'
while opcao in 'Ss':
    num = int(input('Digite um número inteiro: '))
    opcao = str(input('Quer continuar? [S/N]: '))

    if quantidade == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma +=num
    quantidade += 1
    media = soma / quantidade
    if num % 2 == 0:
        cont = 0
        cont+=1
        mediapar = num / cont

print('A média é: {:.2f}, o maior é {} o menor é {}, a quantidade é {}, a média dos pares é {:.2f}'.format(media, maior, menor, quantidade, mediapar))




