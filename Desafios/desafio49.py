n = int(input('Digite um número: '))
print('A tabuada do número {} é: '.format(n))
for i in range(1, 11):
    print('{} X {} = {}'.format(n, i, n * i))
