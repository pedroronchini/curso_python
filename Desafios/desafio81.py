valores = list()
c = ''
n = 0

while True:
    valores.append(int(input('Digite um número: ')))
    c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if c == 'N':
        print('-' * 30)
        print(f'Foram digitados {len(valores)} valores')
        valores.sort(reverse=True)
        print(f'Você adiciounou os valores: {valores}')
        if 5 in valores:
            print('O valor 5 foi digitado')
        else:
            print('O valor 5 não foi digitado')
        break
