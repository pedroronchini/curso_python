def notas(*n, sit=False):
    d = dict()
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['media'] = sum(n) / len(n)
    if sit:
        if d['media'] > 7:
            d['situacao'] = 'BOA'
        elif 7 > d['media'] >= 5:
            d['situacao'] = 'RAZOÁLVEL'
        else:
            d['situacao'] = 'RUIM'
    return d


resp = notas(7.5, 10, 6.5, 2, 7, 4, sit=True)
print(resp)
