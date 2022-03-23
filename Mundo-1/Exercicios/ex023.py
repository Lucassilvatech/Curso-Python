'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados'''

# todo // Respondido apos revisão

#numeros = (input('digite um numero de 0 a 9999:'))
# num = ';'.join(numeros)
# milhar, centena, dezena, unidade = num.split(';')
# print(f'm {milhar} \nc {centena}\n d{dezena}\n u{unidade}')

num = int(input('digite um numereo'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade {u} \nDezena {d} \nCentena {c} \nMilhar {m} ')
