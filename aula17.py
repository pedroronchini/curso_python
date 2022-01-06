a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
"""
num = [2, 5, 9, 1]
valores = list()
for cont in range(0, 5):
  valores.append(int(input('Digite um valor: ')))
valores.append(5)
valores.append(9)
valores.append(4)
num[2] = 3 # substitui valor na posição 2
num.append(7) # adiciona o valor 7 na lista
num.sort() # ordena a lista
num.sort(reverse=True) # ordena a lista reverso
num.insert(2, 2) # insere na lista na posição 2 o valor 2
if 4 in num:
  num.remove(4)
else:
  print('Não achei o número 4')
num.remove(2) remove o primeiro número 2 da lista
num.pop()  remove o ultimo elemento da lista
num.pop(2)  remove o 2 elemento da lista
print(num)
print(f'Essa lista tem {len(num)} elementos. ')
print(valores)
for v in valores:
  print(f'{v}...', end='')
for c, v in enumerate(valores):
  print(f'\nNa posoição {c} encontrei o valor: {v}!', end='')
"""
print(f'Lista A: {a}')
print(f'Lista B: {b}')
