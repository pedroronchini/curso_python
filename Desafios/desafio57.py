s = str(input('Digite o seu sexo (M para masculino e F para feminino): ')).strip().upper()[0]

while s != 'M' and s != 'F':
    print('Você digitou uma opção inválida!')
    s = str(input('Digite novamente o seu sexo (M para masculino e F para feminino: ')).strip().upper()[0]
print('Seu sexo é {}'.format(s))
