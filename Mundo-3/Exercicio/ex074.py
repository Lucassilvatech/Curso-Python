'''criar um programa que que vai getar 5 numeros aleatoris e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor
 e o maior valor que estão na tupla'''

import random
n=0
tupla = 0
for c in range(0,5):
    n = (random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9))

print(f'Eu gerei uma tupla com os numeros {n} o maior numero foi {max(n)}, e o menor numero foi {min(n)}')
