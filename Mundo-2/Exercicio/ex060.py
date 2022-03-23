'''Faça um programa que leia um numero qualquer e mostrar na tela seu fatorial.
ex: 5! = 5x4x3x2x1 = 120'''

'''n = int(input('Digite um numero:'))
v = 1
while n != 1:
    v = v * n
    n = n - 1
    print(v)'''
v = 1
n = int(input('Digite um numero para saber seu fatorial:'))
print(f'{n}! = ',end='')
for c in range(n, 0, -1):
    print(c,end='')
    print(' X ' if c != 1 else print(f' = {v}'),end='')
    v = v * c
