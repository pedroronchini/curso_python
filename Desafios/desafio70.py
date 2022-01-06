n = ''
c = ''
nb = ''
p = 0
t = 0
m = 0
b = 0
count = 0

while True:
    print('-' * 30)
    print('PRODUTOS')
    print('-' * 30)
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$ '))
    count += 1
    print('-' * 30)
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    t += p
    if p >= 1000:
        m += 1
    if count == 1:
        b = p
    else:
        if b > p:
            b = p
            nb = n
    if c == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'O total da compra foi de R${t}')
print(f'Temos {m} custanto mais de R$1000,00')
print(f'O produto mais barato foi {nb} que custa R${b}')
