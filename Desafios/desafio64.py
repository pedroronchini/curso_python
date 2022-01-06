contador = soma = 0

n = int(input('Digite um número[999 para parar]: '))
while n != 999:
    n = int(input('Digite um número[999 para parar]: '))
    soma += n
    contador += 1
print('Foram digitados {} números e a soma deles é {}'.format(contador, soma))
