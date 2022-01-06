numero_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
    'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {numero_extenso[n]}')
        c = str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
        if c != 'S' and c != 'N':
            c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if c == 'N':
            break
    print('Tente novamnete.', end='')
