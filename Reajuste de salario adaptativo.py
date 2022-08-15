salario = float(input('Digite seu salário atual: R$'))

if salario <= 1212:
    print('Você terá 20% de aumento. Seu salário que antes era de R${}, agora será de R${}'.format(salario, (salario*0.2)+salario))

elif 1212 < salario < 2000:
    print('Você terá 15% de aumento. Seu salário que antes era de R${}, agora será de R${}'.format(salario, (salario*0.15)+salario))
else:
    print('Você terá 10% de aumento. Seu salário que antes era de R%{}, agora será de R${}'.format(salario, (salario*0.1)+salario))