from random import choices

alunos = choices(['Jose', 'Maria', 'Joao', 'Ana'], weights=None, k=4)

print('A  ordem dos alunos é {}'.format(alunos))
