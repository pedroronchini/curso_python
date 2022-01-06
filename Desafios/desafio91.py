from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
rank = list()

print('Valores Sorteados:')
for i in range(0, 4):
    jogadores['jogador1'] = randint(1, 7)
    jogadores['jogador2'] = randint(1, 7)
    jogadores['jogador3'] = randint(1, 7)
    jogadores['jogador4'] = randint(1, 7)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:')
for i, v in enumerate(rank):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
