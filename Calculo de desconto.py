preço = float(input('Qual o preço do produto sem desconto? R$'))
desconto = 0.05 * preço
preço2 = preço-desconto

print('O preço do produto com desconto de 5% é de R${:.2f}'.format(preço2))