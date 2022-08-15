from datetime import date
ano = int(input('Digite o ano que deseja saber se é bissexto ou nao. Digite 0 se deseja saber se o ano atual é bissexto: '))


bissexto = ano % 4

if ano == 0:
     ano = date.today().year
if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')