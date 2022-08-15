
analise = {}
analise['nome'] = str(input('Digite seu nome: '))
analise['media'] = float(input('Digite sua média: '))

if analise['media'] >= 7:
    analise['situaçao'] = 'aprovado'

if analise['media'] >= 3 and analise['media'] < 7:
    analise['situaçao'] = 'Você precisa fazer a recuperação'

if analise['media'] < 3:
    analise['situaçao'] = 'Reprovado'

for k, v in analise.items():
    print(f'\n{k}  igual a {v}')