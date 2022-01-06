from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Foi sorteado os valores {n}')
print(f'O maior valor foi {max(n)} e o menor valor foi {min(n)}')
