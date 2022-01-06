# Exemplo aula 22
# Colocar as funções no arquivo uteis.py 
# import uteis
# from uteis import fatorial, dobro
def triplo(n):
    return n * 3


def dobro(n):
    return n * 2


def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
# fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
# print(f'O dobro de {num} é {uteis.dobro(num)}')
