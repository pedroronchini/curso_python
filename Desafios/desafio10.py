carteira = float(input('Digite o quanto de dinhero você tem na carteira? R$ '))

dolar = carteira / 5.12

print('Com R${:.2f} na carteira da para comprar US${:.2f} dolar'. format(carteira, dolar))
