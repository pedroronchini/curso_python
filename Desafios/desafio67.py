n = 0
m = 1

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while m <= 10:
        print(f'{n} X {m} = {m * n}')
        m += 1
print('Programa tabuada encerrado')
