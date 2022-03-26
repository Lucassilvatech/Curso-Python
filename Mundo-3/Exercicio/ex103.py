'''Faça um programa que tenha uma funçao chamada ficha(), que receba o nome de um jogador e quantos gols ele marcou
O programa deverá ser capas de mostrar a ficha do jogador, mesmo que algum dado não tenha cido informado. '''

def ficha (nome = '<desconhecido>', gols=0):
    print('~-'*30)
    print(f'O jogador {nome} fez {gols} gol(s) .')


ficha('Neymar')

ficha(gols=5)

ficha('Neymar',2)

