from random import choice

pessoa = str(input('Escolha entre pedra paepel ou tesoura: '))
maquina = choice(['pedra', 'papel', 'tesoura'])

escolha = maquina

if escolha == 'pedra' and pessoa == 'tesoura':
    print('Você perdeu!')
elif escolha == 'tesoura' and pessoa == 'papel':
    print('Você perdeu!')
elif escolha == 'papel' and pessoa == 'pedra':
    print('Você perdeu!')
elif pessoa == 'pedra' and escolha == 'tesoura':
    print('Você ganhou!')
elif pessoa == 'tesoura' and escolha == 'papel':
    print('Você ganhou!')
elif pessoa == 'papel' and escolha == 'pedra':
    print('Você ganhou!')
