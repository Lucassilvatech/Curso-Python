'''faça um programa que jogue PAR ou IMPAR com o computador. O progama para se o jogador perder,
mostrando quantas vitorias o jogador conseguiu'''
cont = 0
from random import randint
while True:
    n = randint(1, 10)
    player = str(input('Quer Par ou Impar? Digite [I/P]')).strip().lower()
    n1 = int(input(f'Numero que escolheu  {n} [ De 1 a 10]'))
    soma = n + n1
    if soma % 2 == 0:
        res = 'p'
    else:
        res = 'i'
    if player == res:
        print('Você ganhou!!! Vamos jogar novamente.')
        cont += 1
    else:
        print('Você perdeu!')
        break
if cont == 0:
    print('Você teve 0 vitórias .')
elif cont == 1:
    print('Você teve 1 vitória .')
else:
    print(f'Você teve {cont} vitórias consecutivas .')




