aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 7 > aluno['media'] >= 5:
    aluno['situacao'] = 'Recuperção'
else:
    aluno['situacao'] = 'Reprovado'
print('-' * 40)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')