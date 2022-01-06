s = c = ''
sm = sh = si = i = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F]')).strip().upper()[0]
    while s != 'M' and s != 'F':
        s = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 30)
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 30)
    if i >= 18:
        si += 1
    if s == 'M':
        sh += 1
    if s == 'F':
        if i < 20:
            sm += 1
    if c == 'N':
        break
print('====== FIM DO PROGRAMA ======')
print(f'Total de pessoas com mais de 18 anos: {si}')
print(f'Ao todo temos {sh} homen(s) cadastrado')
print(f'E temos {sm} mulher(es) com menos de 20 anos')
