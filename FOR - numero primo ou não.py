
for num in range(1,6):
    num = int(input('Digite um número: '))
    if num % 2 != 0 and num %3 != 0 and num %5 !=0:
        print('{} é primo'.format(num))

