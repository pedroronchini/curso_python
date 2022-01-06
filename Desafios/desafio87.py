matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = sc = m = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
print('-' * 30)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^5}]', end='')
        if matriz[i][j] % 2 == 0:
            s += matriz[i][j]
    print()
print('-' * 30)
print(f'A soma dos valores pares é {s}')
for i in range(0, 3):
    sc += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {sc}')
for j in range(0, 3):
    if j == 0:
        m = matriz[1][j]
    elif matriz[1][j] > m:
        m = matriz[1][j]
print(f'O maior valor da segunda linha é {m}')
