''' mostrar se um ano é bissexto'''

#feito após revisão

'''va = int(input('Digite um ano que queira saber se é bissexto:')) # correto, porrem imcompleto. feito só
ano = va % 4
if ano == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto')'''

from datetime import date

va = int(input('Digite um ano que queira saber se é bissexto:'))
if va == 0:
    va =  date.today().year

if va % 4 == 0 and va % 100 != 0 or va % 400 == 0:
    print(f'O ano de {va} é bissexto!')
else:
    print(f'O ano de {va} não é bissexto!')