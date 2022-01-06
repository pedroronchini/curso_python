# Exemplo aula 23

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dadados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir o número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as error:
    print(f'O erro encontrado foi {error.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre')
