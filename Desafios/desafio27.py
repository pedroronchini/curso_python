nome = input('Digite seu nome completo: ').strip()
lista = nome.strip().split()
print('Primeiro nome: {} \nÚltimo nome: {}'.format(lista[0], lista[-1]))
