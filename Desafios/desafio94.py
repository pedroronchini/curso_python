pessoa = dict()
grupo = list()
m = s = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]

    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('ERROR! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    grupo.append(pessoa.copy())
    r = str(input('Deseja continuar? [S/N] ')).upper()[0]

    while r != 'S' and r != 'N':
        r = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if r == 'N':
        m = s / len(grupo)
        break

print('-' * 40)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {m:5.2f} anos.')
print(f'- As mulheres cadastradas foram ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= m:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')
