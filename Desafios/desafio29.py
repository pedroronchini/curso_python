velocidade = float(input('Qual a velocidade do carro:  '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado! O valor da multa é de R${:.2f}'.format(multa))
