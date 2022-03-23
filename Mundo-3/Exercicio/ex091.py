'''Crie um programa onde 4 jogadores vão jogar um dado e tenham resultados aleatorios.
Guarde esses resultados em um dicionario. No final coloque esse disionario em ordem
sabendo que o vencedor tirou o maior numero no dado'''

from random import randint
Jogo = dict()
print('  Valores sorteados:')
for c in range(0,4):
    Jogadores = randint(1,6)
    print(f'    jogador{c+1} tirou {Jogadores}')
    Jogo[f'Jogador{c+1}'] = Jogadores
cont = 0
print('  Ranking dos jogadores:')
for i in sorted(Jogo, key = Jogo.get,reverse=True):
    cont +=1
    print(f'    {cont}º lugar: {i} com {Jogo[i]} pontos')

