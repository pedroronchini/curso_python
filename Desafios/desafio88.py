from random import randint

print('-' * 40)
print('{:^20}'.format('JOGO NA MEGA SENA'))
print('-' * 40)

n = int(input('Quantos jogos você que que eu sorteie?  '))
jogos = list()

for i in range(n):
    jogos.append(list())
    for c in range(0, 6):
        r = randint(1, 60)
        if r not in jogos:
            jogos[i].append(r)
    print(f'Jogo {i}: {jogos[i]}')
print('-' * 40)
