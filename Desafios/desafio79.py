valores = list()
c = ''
n = 0

while True:
    n = (int(input('Digite um número: ')))
    if n in valores:
        print('Valor duplicado! Não vou adicionar')
    else:
        valores.append(n)
        print('O valor foi adicionado')
    c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        valores.sort()
        print(f'Você adiciounou os valores: {valores}')
        break
