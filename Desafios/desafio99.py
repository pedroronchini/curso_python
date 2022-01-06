from time import sleep


def linha():
    print('-' * 50)


def maior(*num):
    linha()
    print('Analisando os valores passados...')
    pos = 0
    maior = 0
    for i in num:
        print(f'{i} ', end='')
        pos += 1
        if pos == 0:
            maior = pos
        else:
            if maior < i:
                maior = i
        sleep(0.5)
    print(f'Foram informados {pos} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
