'''Ler um número inteiro e dizer se ele é ou não um numero primo.'''
'''s = 0
n = int(input('Digite um valor para saber se ele é ou não um numero primo:'))
for c in range(1,n+1):
    if n % c == 0:
        s = s + c
if s == n+1:
    print(f'O numero {n} é primo!')
else:
    print(f'O numero {n} não é primo.')'''

# Forma que foi feito no correção
s = 0
n = int(input('Digite um valor para saber se ele é ou não um numero primo:'))
for c in range(1,n+1):
    if n % c == 0:
        s = s + 1
if s == 2:
    print(f'O numero {n} é primo!')
else:
    print(f'O numero {n} não é primo.')
