jogador = dict()
gols = list()
jogadores = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogo? '))
    gols.clear()
    for i in range(p):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while r != 'S' and r != 'N':
        r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
# Cabeçalho
print('-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)
for k, v in enumerate(jogadores):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERROR! Não existe o jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}: ')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
