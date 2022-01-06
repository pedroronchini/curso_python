from time import sleep


def linha():
    print('-' * 30)


def contador(inicio, fim, passo):
    linha()
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(f'{i} ', end='')
            sleep(0.5)
        print('FIM')
    if inicio > fim:
        for i in range(inicio, fim - 1, - passo):
            print(f'{i} ', end='')
            sleep(0.5)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
