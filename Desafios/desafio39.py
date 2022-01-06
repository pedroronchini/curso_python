import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

nascimento = int(input('Em qual ano você nasceu?  '))
ano = date.strftime("%Y")
anoInt = int(ano)
idade = anoInt - nascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print('Você ainda vai se alistar!')
elif idade > 18:
    print('Já passou a hora de se alistar!')
