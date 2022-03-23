'''Aprimore o exercicio 093 para que ele funcione com varios jogadores,
incluindo um sistema de detalhes do aproveitamento de cada jogador. '''

copia = list()
while True:
    gols = list()
    jogadores = dict()
    jogadores['Nome'] = str(input('Nome do jogador:'))
    partidas = int(input('Quantas patidas jogou?'))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols na {c+1}ª partida?')))
    jogadores['gols'] = gols
    copia.append(jogadores.copy())
    ttgols = 0
    while True:
        sair = str(input('Gostaria de continuar? [S/N]')).strip().upper()[0]
        if sair not in 'SN':
            print('ERRO! Digite somente SIM ou NÃO.')
        else:
            break
    if sair == 'N':
        break


print(copia)
for pos, i in enumerate(copia):
    for l in i['gols']:
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

