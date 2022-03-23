'''melhorar o desafio 28, agora o jogador vai tentar até acertar ,mostrando no final quantos palpites foram necessarios
para vencer'''

import random
p = 1
m = random.randint(0,10)
j = int(input(f'Em que numero estou pensando?'))
while j != m:
    if j < m:
        j = int(input('Maior...Tente novamente:'))
    else:
        j = int(input('Menor...Tente novamente:'))
    p+= 1
print('PARABÊNS, Você acertou!!')
print(f'você precisou de {p} tentativas para ganhar.')


