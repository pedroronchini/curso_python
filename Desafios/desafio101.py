def voto(ano):
    from datetime import date
    now = date.today().year
    i = now - ano

    if i >= 18:
        return f'Com {i} anos: VOTO OBRIGATÓRIO'
    elif 16 <= i < 18 or i > 65:
        return f'Com {i} anos: VOTO OPCIONAL'
    else:
        return f'Com {i} anos: NÃO VOTA'


idade = int(input('Em que ano você nasceu? '))
voto(idade)
