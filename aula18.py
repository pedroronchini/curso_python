"""
teste = list()
teste.append('Pedro')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
  print(p)
  print(p[0])
  print(f'{p[0]} tem {p[1]} anos de idade')
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
"""
galera = list()
dados = list()
totmai = totmen = 0
for i in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')
