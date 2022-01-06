from random import randint

computador = randint(0, 5)

print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
numero = int(input('Em que número pensei? '))

if numero == computador:
    print('Você acertou!')
else:
    print('Você errou! O número que eu pensei foi {} e não {}'.format(computador, numero))
