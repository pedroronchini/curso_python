numero = int(input('Digite um número: '))
escolha = int(input('Escolha uma das opções: 1- Para binário, 2- Para Octal e 3- Para hexadecimal'))

if escolha == 1:
    binario = bin(numero)
    print(binario)
elif escolha == 2:
    octa = oct(numero)
    print(octa)
elif escolha == 3:
    hexadecimal = hex(numero)
    print(hexadecimal)
