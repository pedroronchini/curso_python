def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def aumentar(n=0, d=0, f=False):
    v = 0
    v = n + (n * d / 100)
    if f:
        return moeda(v)
    return v


def diminuir(n=0, d=0, f=False):
    v = 0
    v = n - (n * d / 100)
    if f:
        return moeda(v)
    return v


def metade(n=0, f=False):
    v = 0
    v = n / 2
    if f:
        return moeda(v)
    return v


def dobro(n=0, f=False):
    v = 0
    v = n * 2
    if f:
        return moeda(v)
    return v


p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando 10% temos {aumentar(p, 10, True)}')
print(f'Reduzindo 13% temos {diminuir(p, 13, True)}')
