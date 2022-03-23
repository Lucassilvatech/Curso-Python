''' O programa vai ter que mostrar se um jovem esta na hora do alistamento, se ja passou o tempo ou se ainda vai.
O programa devera mostrar o tempo que falta ou que passou '''

# Pegar a data da maquina
'''from datetime import date

today = date.today().year

# Pegar ano de nascimento da pessoa
ano = int(input('Em que ano você nasceu?'))
va = ano + 18
if va > today:
    print(f'Ainda faltam {va - today} anos para o seu alistamento.')
elif va < today:
    print(f'ja passou {today - va} anos do seu alistamento. ')
else:
    print('Parabéns. Esse ano vomos carpir umas ruas!!!!!')'''

from datetime import date

today = date.today().year

s = str(input('Qual o seu sexo? RESPONDA COM "F" OU "M":')).upper()

if s == 'M':
    ano = int(input('Em que ano você nasceu?'))
    va = ano + 18
    if va > today:
        print(f'Você tem {today - ano} anos e faltam{va - today} anos para o seu alistamento.')
    elif va < today:
        print(f'Você tem {today - ano} anos e ja passou {today - va} anos do seu alistamento. ')
    else:
        print('Parabéns. Esse ano vomos carpir umas ruas!!!!!')
else:
    print('Você não precisa se alistar para as forças armadas.Obrigado')