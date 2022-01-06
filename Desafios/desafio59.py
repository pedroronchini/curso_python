n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = int(
    input('Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))

while menu != 5:
    if menu == 1:
        print('A soma dos números {} e {} é {}'.format(n1, n2, n1 + n2))
        menu = int(input(
            'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
    if menu == 2:
        print('A multiplicação entre {} e {} é igual a: {}'.format(n1, n2, n1 * n2))
        menu = int(input(
            'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
    if menu == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
            menu = int(input(
                'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
        else:
            print('O maior número é {}'.format(n2))
            menu = int(input(
                'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
    if menu == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        menu = int(input(
            'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
    if menu == 5:
        print('Você saiu do programa!')
    else:
        print('Opção errada, digite um valor entre 1 e 5!')
        menu = int(input(
            'Selecione uma opção:\n [1] Somar\n [2] multiplicar\n [3] Maior\n [4]Novos números\n [5]Sair do programa\n'))
