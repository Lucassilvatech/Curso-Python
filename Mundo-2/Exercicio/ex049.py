'''Refazer o desafio 9 utilizando laço for'''
n = int(input('digite um valor para saber sua taboada:'))
for c in range(1,11):
    print(f'{n} x {c} = {n * c}')