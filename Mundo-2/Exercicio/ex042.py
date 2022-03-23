''' Refazer exercicio 35 acrescentando o tipo do triângulo
- equilátero: todos os lados iquais
- isósceles: dois lados iquais
- escaleno: todos os lados diferentes'''

'''r1 = int(input('Digite um valor:'))
r2 = int(input('Digite um valor:'))
r3 = int(input('Digite um valor:'))

if r1 == r2 and r1 != r3 and r2 == r1 and r2 != r3 or r3 == r1 and r3 != r2 and r1 == r3 and r1 != r2:
    triangulo = 'isórceles'
elif r3 == r2 and r3 != r1 and r2 == r3 and r2 != r1:
     triangulo = ' isórceles'
elif r1 == r2 == r3:
    triangulo = 'equilátero'
else:
    triangulo = 'escaleno'

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Esaas retas formam um triângulo {triangulo}')

else:
    print('Essas retas não formam um triângulo')'''

r1 = int(input('Digite um valor:'))
r2 = int(input('Digite um valor:'))
r3 = int(input('Digite um valor:'))

if r1 == r2 ==r3:
    triangulo = 'equilátero'
elif r1 != r2 and r1 != r3 and r2 != r3:
    triangulo = 'escaleno'
else:
    triangulo = 'ísosceles'

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Esaas retas formam um triângulo {triangulo}')

else:
    print('Essas retas não formam um triângulo')



