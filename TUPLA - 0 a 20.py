cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if  0 <= num <= 20:
        break
    print('Digite um valor válido.', end='')
    
print(f'Você digitou o número {cont[num]}')
