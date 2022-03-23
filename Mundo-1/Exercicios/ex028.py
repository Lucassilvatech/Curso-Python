'''O computador tem que "pensar" em um numero inteiro de 0 a 5 e pedir para o usuario tentar descobrir qual foi
o numero escolhido '''
# O programa devera escrever na tela se o usuário venceu ou perdeu.

import random

from time import sleep

n = random.randint(0,5) #
num = int(input('Em que numero de 0 á 5 estou "pensando"?'))
print('processando...')
sleep(1.5)
if n == num:
    print('Você venceu! PARABÉNS', )
else:
    print(f'Eu te venci! ^_^ . Eu "pensei" no numero {n} e não no {num}')


