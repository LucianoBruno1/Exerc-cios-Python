km = float(input('Digite quantos quilômetros você rodou com o carro: '))
dias = int(input('Digite quantos dias você ficou com o carro: '))
diaria = 60 * dias
tarifa = 0.15 * km
total = diaria + tarifa

print('\n Seus gastos foram: ')
print(' R${} Pelos dias rodados'.format(diaria))
print(' R${} pelos quilômetros rodados'.format(tarifa))
print('\n O total a pagar é R${}'.format(total)?)