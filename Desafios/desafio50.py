soma = 0
for i in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(i)))
    if num % 2 == 0:
        soma += num
print('A soma de todos os número é {}'.format(soma))
