distancia = float(input('Qual a distancia em Km da viagem?   '))

if distancia <= 200:
    custo = distancia * 0.50
    print('O custo da viagem é de R${:.2f}'.format(custo))
else:
    custo = distancia * 0.45
    print('O custo da viagem é de R${:.2f}'.format(custo))
