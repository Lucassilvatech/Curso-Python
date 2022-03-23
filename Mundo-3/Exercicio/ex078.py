'''faça um programa que leia 5 valores numericos e guardeos em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

num =[]
for c in range(0,5):
    num.append(int(input('Digite um valor:')))
max = max(num)
min = min(num)
print(f'O maior valor é {max} e aparece nas posições ',end='')
for cont, ci in enumerate(num):
    if max == ci:
        print(f'{cont}...',end='')
print(f'\no menor valor é o {min} e aparece nas posições ',end='')
for cont, ci in enumerate(num):
    if min == ci:
        print(f'{cont}...',end='')
