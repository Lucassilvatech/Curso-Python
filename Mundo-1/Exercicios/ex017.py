'''from math import sqrt
n1 = float(input('digite o cateto:'))
n2 = float(input('digite o cateto oposto:'))
r1 = n1 ** 2
r2 = n2 ** 2
rr = r1 + r2
f = sqrt(rr)
print(f'O valor da hipotenusa é {f:.2f}')'''


from math import hypot
n1 = float(input('Digite o cateto adjacente:'))
n2 = float(input('Digite o cateto oposto'))
f = hypot(n1,n2)
print(f'{f}')