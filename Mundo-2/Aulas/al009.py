# Estrutura de repetição

''' laço c no intervalo (1,10):
    passo
pega

for c in range(1,10):
    passo
pega'''

'''print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')
print('Oi')'''

'''for c in range(0,6):
    print('Oi')
print('end')
for c in range(0,6):
    print(c)
print('end')
for c in range( 6,0,-1):
    print(c)
print('end')
for c in range(8,-1,-1):
    print(c)
print('end')
from time import sleep
for c in range(0,6 +1):
    sleep(0.4)
    print(c)'''
i = int(input('inicio:'))
f = int(input('fim:'))
p = int(input('passo:'))
for c in range(i,f+1,p):
    print(c)

s = 0
for c in range(0,10):
    n = int(input('digite um valor:'))
    s = s + n
print(s)





