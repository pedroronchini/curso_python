from random import randint;

computador = randint(0, 10)
tentativas = 0

print('Vou pensar em um número de 0 a 10. Tente adivinhar...')
numero = int(input('Em que número pensei? '))
if numero == computador:
    print('Você acertou! E precisou de {} tentativas para acertar!'.format(tentativas))
else:
    while numero != computador:
        tentativas += 1
        print('Você errou!')
        numero = int(input('Tente novamente: '))
    print('Você acertou! E precisou de {} tentativas para acertar!'.format(tentativas))
