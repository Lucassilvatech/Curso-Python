'''Ler o peso de 5 pessoas e mostrar quais são o maior e menor peso'''

'''n = 0
k = ''
for c in range(0, 5):
    peso = str(input('Qual seu peso:'))
    k = k + ' ' + peso
j = (k).split()
# j = (list(j))
l = max(j)
u = min(j)
print(f'{j} {l}  {u}')
   # if peso > l:
 #  l = pes'''
l = 0
k = 0
for c in range(0,5):
    p = float(input('Qual seu peso:'))
    if c == 1:
        l = p
        k = p
    else:
        if p > l:
            l = p
        if p < k:
            k = p
print(f'O maior peso foi {l}Kg e o menor peso foi {k}Kg')