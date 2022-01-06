n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
lista = (n1, n2, n3, n4)
count = 0

print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in lista:
    if n % 2 == 0:
        count += 1
print(f'Os valores pares digitados foram {count}')
