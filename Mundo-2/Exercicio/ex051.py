'''Ler o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progrssão '''

#bugado
'''pt = int(input('ponto inicial'))
r = int(input('razão'))
l = r * 11
for c in range(pt,l, r):
    print(f'{c}')'''

#feito apos correção
pt = int(input('ponto inicial'))
r = int(input('razão'))
i = pt + (10 - 1) * r
for c in range(pt,i + r,r):
    print(f' {c}', end='-=-')

