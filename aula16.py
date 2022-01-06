lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
"""
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
pessoa = ('Pedro', 21, 'M', 70.50)
print(pessoa)
print('-' * 30)
print(c)
print(d)
print(len(c))
print(d.count(5))
print(d.index(8))
print(d.index(5, 1))
print('-' * 30)
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(len(lanche))
print(sorted(lanche))
print('-' * 30)
for count in range(len(lanche)):
  print(f'Eu vou comer {lanche[count]} na posição {count}')
print('-' * 30)
for comida in lanche:
  print(f'Eu vou comer {comida}')
print('-' * 30)
"""
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-' * 30)
