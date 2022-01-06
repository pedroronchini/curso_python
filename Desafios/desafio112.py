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


def resumo(n=0, a=10, r=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'O dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{r}% de redução: \t{diminuir(n, r, True)}')
    print('-' * 35)


def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERROR! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


p = leiaDinheiro('Digite o preço: R$ ')
resumo(p, 20, 12)
