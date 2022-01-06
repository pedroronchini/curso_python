primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro_termo
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
