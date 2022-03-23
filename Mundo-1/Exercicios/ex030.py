'''Tem que mostrar se um numero  inteiro é impar ou par'''

num = int(input('Digite um numero:'))
numero = num%2
if numero == 0:
    print('Esse numero é par!')
else:
    print('Esse numero é impar!')