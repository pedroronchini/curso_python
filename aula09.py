frase = 'Curso em Vídeo Python'
frase1 = '    Curso em Vídeo Python    '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase1))
print(len(frase1.strip()))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])