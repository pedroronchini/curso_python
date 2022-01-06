lista = list()
par = list()
impar = list()
c = ''

while True:
    lista.append(int(input('Digite um valor: ')))
    c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print('-' * 30)
for v in lista:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')
