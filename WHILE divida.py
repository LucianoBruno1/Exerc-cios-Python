
valor_inicial = float(input('Informe o valor inicial: R$'))
juros = float(input('informe o juros: '))
valor_mensal = float(input('Valor mensal a ser pago: '))

juros_pago = 0
mes = 1
valor_pago_total = 0
juros_mensal_pago = valor_inicial * juros
divida = valor_inicial + (valor_inicial * juros_mensal_pago)
divida = divida - valor_mensal

print('{} - {} | {}'.format(mes, divida, valor_mensal))


while divida > 0:
    juros_mensal_pago = divida * juros
    divida = divida + juros_mensal_pago
    juros_pago += juros_mensal_pago

    if divida <= valor_mensal:
        divida = 0
        valor_pago_total += divida
    else:
        divida = divida - valor_mensal
        valor_pago_total += valor_mensal
    mes+=1
print('{} - {} | {}'.format(mes, divida, valor_mensal))