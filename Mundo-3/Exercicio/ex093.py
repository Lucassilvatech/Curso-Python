'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
 e quantas partidas ele jogou depois vai ler a quantidade de gols feito em cada partida.
 No final tudo isso sera guardado em um dicionario incluindo a quantida de de gols feitos no campeonato'''
gols = list()
jogadores = dict()
jogadores['Nome'] = str(input('Nome do jogador:'))
partidas = int(input('Quantas patidas jogou?'))
for c in range(0,partidas):
    gols.append(int(input(f'Quantos gols na {c+1}ª partida?')))
jogadores['gols'] = gols
ttgols = 0
for l in gols:
    ttgols += l
jogadores['total'] = ttgols
print('-'*35)
print(jogadores)
print('-'*35)
for kay, i in jogadores.items():
    print(f'O campo {kay} tem o valor {i} .')
print('-'*35)
print(f'  O jogador {jogadores["Nome"]} jogou {partidas} partidas')
for pos, item in enumerate(jogadores['gols']):
    print(f'    => No {pos+1}º jogo fez {item} gol(s) .')

