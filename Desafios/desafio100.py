from random import randint
from time import sleep


def sorteia():
    n = list()
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        n.append(randint(0, 10))
        sleep(0.5)
        print(f'{n[i]} ', end='')
    print('PRONTO!')
    return n


def somaPar(n):
    s = 0
    for i in n:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {n}, temos {s}')


a = sorteia()
somaPar(a)
