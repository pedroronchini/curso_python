jogador = dict()
gols = list()
s = 0

jogador['nome'] = str(input('Nome do Jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogo? '))

for i in range(p):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    s += gols[i]
jogador['gols'] = gols
jogador['total'] = s
print('-' * 40)
print(jogador)
print('-' * 40)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 40)
print(f'O Jogador {jogador["nome"]} jogou {p} partidas.')

for i, c in enumerate(gols):
    print(f'{"=>":>4} Na partida {i}, fez {c} gols.')
print(f'Foi um total de {jogador["total"]} gols')
