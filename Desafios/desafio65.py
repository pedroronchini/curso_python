n = count = media = soma = maior = menor = 0
c = 'S'

while c != 'N':
    n = int(input('Digite um número: '))
    c = str(input('Deseja continua? [S/N] ')).strip().upper()[0]
    soma += n
    count += 1
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / count
print('Você digitou {} números e a média foi {:.2f}'.format(count, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
