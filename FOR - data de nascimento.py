cont = 0
cont2 = 0
for ano in range(1,8):
    cont+=1
    ano = int(input('Digite seu ano de nascimento: '))
    if 2022 - ano >= 18:
        cont2+=1
print('Das {} pessoas, {} são maiores de idade.'.format(cont, cont2))