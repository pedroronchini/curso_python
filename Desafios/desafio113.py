def leiaInteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Digite um número inteiro válido!')
            continue
        except KeyboardInterrupt:
            print('O usuário não quis continuar digitando!')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('Digite um valor real válido!')
            continue
        except KeyboardInterrupt:
            print('O usuário não quis continuar digitando!')
            return 0
        else:
            return f


n = leiaInteiro('Digite um valor inteiro: ')
f = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n} e o valor real foi {f}')
