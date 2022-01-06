# Exemplo aula 21
"""
help(input)
print(input.__doc__)
def contador(i, f, p):
    -> Faz uma contagem e mostra na tela
    # :param i: inicio da contagem
    # :param f: fim da contagem
    # :param p: passo da contagem
    # :return: sem retorno
  c = i
  while c <= f:
    print(f'{c} ', end='')
    c += p
  print('FIM')
help(contador)
def soma(a=0, b=0, c=0):
    -> Faz uma contagem e mostra na tela
    # :param a: o primeiro valor
    # :param b: o segundo valor
    # :param c: o terceiro valor
    # :return: sem retorno
  s = a + b + c
  print(f'A soma vale {s}')
soma()

def funcao():
  n1 = 4
  print(f'n1 dentro vale {n1}')
n1 = 2
funcao()
print(f'n1 fora vale {n1}')
def soma(a=0, b=0, c=0):
  s = a + b + c
  return s
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')
"""


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}')
