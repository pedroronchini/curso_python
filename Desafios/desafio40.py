numero1 = float(input('Digite a primeira nota: '))
numero2 = float(input('Digite a sua segunda nota: '))
media = (numero1 + numero2) / 2

if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO')
elif media > 7.0:
    print('APROVADO')
