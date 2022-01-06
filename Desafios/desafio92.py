from datetime import date

data = date.today().strftime('%Y')
a = int(data)
pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
n = int(input('Ano de nascimento: '))
d = a - n
pessoa['idade'] = d
pessoa['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
print('-' * 30)
if pessoa['ctps'] == 0:
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
else:
    pessoa['contratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - a)
    print('-' * 30)
    for k, v in pessoa.items():
        print(f'{k} tem o valor {v}')
