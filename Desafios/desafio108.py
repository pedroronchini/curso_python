def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')


def aumentar(n=0, a=0):
    return n + (n * a / 100)


def diminuir(n=0, d=0):
    return n - (n * d / 100)


def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10% temos {moeda(aumentar(p, 10))}')
print(f'Reduzindo 13% temos {moeda(diminuir(p, 13))}')
