primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro_termo
cont = 1

while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo = termo + razao
    cont += 1
print('Fim')
