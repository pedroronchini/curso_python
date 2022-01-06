preco = float(input('Digite o preço do produto: '))
forma_pagamento = int(input(
    'Digite a forma de pagamento( 1- Á vista dinheiro/cheque, 2- Á vista cartão, 3- 2x no cartão, 4 - 3x ou mais) '))

if forma_pagamento == 1:
    desconto = preco * 0.1
    valor = preco - desconto
    print('O valor vai ser {:.2f}'.format(valor))
elif forma_pagamento == 2:
    desconto = preco * 0.05
    valor = preco - desconto
    print('O valor vai ser {:.2f}'.format(valor))
elif forma_pagamento == 3:
    print('O valor vai ser {:.2f}'.format(preco))
elif forma_pagamento == 4:
    quantidade = int(input('Em quantas vezes vai ser o pagamento? '))
    valor = preco + (preco * 0.2)
    valor_parcela = (preco + (preco * 0.2)) / quantidade
    print('O valor vai ser {:.2f}, para ser pago em {} vezes de {:.2f} '.format(valor, quantidade, valor_parcela))
