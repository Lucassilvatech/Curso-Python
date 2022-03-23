''' A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria de acordo com sua idade.
- Até 9 anos mirim
- Até 14 anos infantil
- Até 19 anos junior
- Até 20 anos sénior
- acima master'''

from datetime import date

today = date.today().year
nascimento = int(input('Que ano você nasce?'))
l = today - nascimento
if l <= 9:
    cate = 'mirim'
elif l >= 10 and l <= 14:
    cate = 'infantil'
elif l >= 15 and l <= 19:
    cate = 'junior'
elif l > 19 and l < 21:
    cate = 'sénior'
else:
    cate = 'master'

print(f'Você esta na categoria {cate}!')

