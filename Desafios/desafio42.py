r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

s1 = r2 - r3
s2 = r2 + r3
s3 = r1 - r3
s4 = r1 + r3
s5 = r1 - r2
s6 = r1 + r2

if (s1 < r1 < s2) and (s3 < r2 < s4) and (s5 < r3 < s6):
    print('As três retas formam um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('As três retas não formam um triângulo')
