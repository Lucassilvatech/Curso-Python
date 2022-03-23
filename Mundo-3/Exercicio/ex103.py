'''Faça um programa que tenha uma funçao chamada ficha(), que receba o nome de um jogador e quantos gols ele marcou
O programa deverá ser capas de mostrar a ficha do jogador, mesmo que algum dado não tenha cido informado. '''

def ficha (nome, gols=0):
    nome = '<desconhecido>'
    print('~-'*30)
    nome = str(input('Nome do jogador:'))
    gols = int(input('Quantidade de gols'))
    print(f'O jogador {nome} fez {gols} gol(s) .')


#programa principal
nome = 'Lucas'#str(input('Nome do jogador:'))
gols = int(input('Quantidade de gols:'))
ficha('Lucas', 5)
