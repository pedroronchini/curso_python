vdc = int(input('Qual é o valor da casa?  '))
s = int(input('Qual é o seu salário?  '))
qa = int(input('Quantos anos você vai pagar?  '))

pm = vdc / qa
ex = (s * 30) / 100

if pm >= ex:
    print('Emprestimo negado pois execedu 30% do seu salário!')
else:
    print('Empréstimo aceito!')
