numero = int(input('Digite um número: '))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

print('\nO número {} foi divisível {} vezes.'.format(numero, total))

if total == 2:
    print('Por isso o número {} é primo!'.format(numero))
else:
    print('Por isso o número {} não é primo!'.format(numero))
