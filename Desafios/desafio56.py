soma = 0
media = 0
maior = 0
nomeVelho = ''
total = 0

for i in range(1, 5):
    print('----- {}° Pessoa -----'.format(i))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()

    soma += idade

    if i == 1 and sexo in 'Mm':
        maior = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maior:
        maior = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        total += 1

media = soma / 4

print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, nomeVelho))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(total))
