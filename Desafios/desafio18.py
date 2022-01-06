from math import sin, cos, tan, radians

n = int(input('Digite um angulo:  '))

print('O seno, cosseno e tangente do angulo {} é {}, {}, {}'.format(n, sin(radians(n)), cos(radians(n)), tan(radians(n))))
