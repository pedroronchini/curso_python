import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()

nascimento = int(input('Em qual ano você nasceu?  '))
ano = date.strftime("%Y")
anoInt = int(ano)
idade = anoInt - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
