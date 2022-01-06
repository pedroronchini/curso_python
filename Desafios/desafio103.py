def ficha(nome='', gols=''):
    if nome == '' and gols == '':
        nome = '<desconhecido>'
        gols = '0'
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif nome == '':
        nome = '<desconhecido>'
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif gols == '':
        gols = '0'
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    else:
        return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


j = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
ficha(j, g)
