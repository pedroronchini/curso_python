altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso, o resultado do IMC é {:.2f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('Peso ideal, o resultado do IMC é {:.2f}'.format(imc))
elif 25 < imc <= 30:
    print('Sobrepeso, o resultado do IMC é {:.2f}'.format(imc))
elif 30 < imc <= 40:
    print('Obesidade, o resultado do IMC é {:.2f}'.format(imc))
else:
    print('Obesidade mórbida, o resultado do IMC é {:.2f}'.format(imc))
