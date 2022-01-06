maior_peso = 0
menor_peso = 0

for i in range(0, 5):
    peso = float(input('Digite seu peso:'))
    if peso > maior_peso:
        maior_peso = peso
    else:
        menor_peso = peso

print('O maior peso é {} Kg'.format(maior_peso))
print('O menor peso é {} Kg'.format(menor_peso))
