from datetime import date

soma = 0
menor = 0

ano_atual = date.today().year

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano
    if idade >= 21:
        soma += 1
    else:
        menor += 1

print('O número de pessoas que são maior de idade é {}'.format(soma))
print('O número de pessoas que são menores de idade é {}'.format(menor))
