from random import randint

c = randint(0, 9)
e = ''
count = s = n = 0

while True:
    n = int(input('Digite um valor: '))
    e = str(input('PAR ou ÍMPAR ? [P/I]')).strip().upper()[0]
    s = n + c
    if s % 2 == 0 and e == 'P':
        print(f'Você jogou {n} e o computador {c}. Total de {s} deu PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente ...')
        count += 1
    if s % 2 == 0 and e == 'I':
        print(f'Você jogou {n} e o computador {c}. Total de {s} deu PAR')
        print('Você PERDEU!')
        break
    if s % 2 == 1 and e == 'I':
        print(f'Você jogou {n} e o computador {c}. Total de {s} deu IMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente ...')
        count += 1
    if s % 2 == 1 and e == 'P':
        print(f'Você jogou {n} e o computador {c}. Total de {s} deu PAR')
        print('Você PERDEU!')
        break
print('GAME OVER!')
print(f'Você venceu {count} vezes.')
