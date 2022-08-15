dados = {}
aposentadoria = 0
idade = 0
dados['nome'] = str(input('Digite seu nome: '))
dados['ano de nascimento'] = int(input('Digite o ano em que você nasceu: '))
dados['Carteira de trabalho'] = int(input('Digite o n° da sua carteira de trabalho (0 se não tiver): '))

if dados['Carteira de trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Digite o ano em que você foi contratado(a): '))
    dados['salario'] = int(input('Digite seu salário: '))

for k, v in dados.items():
    print(f'- {k} tem o valor {v}')
idade = 2022 - dados['ano de nascimento']
print(f'- A idade tem o valor {idade}')
