numeros = [[], []]

for i in range(1, 8):
    n = int(input(f'Digite o {i}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f'Os valores ímpares digitados foram: {numeros[1]}')
