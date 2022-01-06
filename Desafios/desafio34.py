salario = float(input('Digite seu salário:  '))

if salario > 1250.00:
    aumento = salario * (110 / 100)
    print('O seu novo salário com o aumento de 10% é de R${:.2f}'.format(aumento))
else:
    aumento = salario * (115 / 100)
    print('O seu novo salário com o aumento de 15% é de R${:.2f}'.format(aumento))
