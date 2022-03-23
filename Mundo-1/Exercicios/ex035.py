'''Desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem ou não formar um triângulo'''

'''r1 = int(input('Digite o comprimento da reta 1 :'))
r2 = int(input('Comprimento da reta 2 :'))
r3 = int(input('Cumprimento da reta 3 :'))


m1 = r1 + r2 > r3
m2 = r1 + r3 > r2
m3 = r3 + r2 > r1
l = m1,m2,m3
if l == (True, True, True):
    print('Essas retas formam um triâmgulo!')
else:
    print('Essas retas não formam um triângulo!')'''

r1 = int(input('Digite o comprimento da reta 1 :'))
r2 = int(input('Comprimento da reta 2 :'))
r3 = int(input('Cumprimento da reta 3 :'))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print('Essas retas formam um triangulo!')

else:
    print('Não, essas retas não formam um triâmgulo!')