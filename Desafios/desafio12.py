preco = float(input('Digite o preço do produto:  '))

desconto = preco - (preco * (5 / 100))

print('O seu novo preço com desconto de 5% é {:.2f}'.format(desconto))
