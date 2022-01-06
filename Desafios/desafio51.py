primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = primeiro_termo + (10 - 1) * razao
soma = 0
for i in range(primeiro_termo, decimo + razao, razao):
    soma = primeiro_termo + razao
    print(i, end='-> ')
print('Acabou!')
