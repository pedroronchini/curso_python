def aumentar(n, a):
    return n + (n * a / 100)


def diminuir(n, d):
    return n - (n * d / 100)


def metade(n):
    return n / 2


def dobro(n):
    return n * 2


p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10% temos {aumentar(p, 10)}')
print(f'Reduzindo 13% temos {diminuir(p, 13)}')
