def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.2f}m².')


largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
