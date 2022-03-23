'''Criar uma tupla com os 20 primeiros colocados do brasileirão na ordem de colocação
depois mostre:
a) apenas os 5 primeiros colocados
b) Os 4 ultimos colocados
c) uma lista com os times em ordem alfabetica
d) em que posição está a chapecoense'''

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
'Atlético-GO','Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude',
'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os 5 primeiros colocados são {times[0:5]} ')
print(f'Os quatro ultimos colocados são {times[-4:]}')
print(f'Os times em ordem alfabetica são {sorted(times)}')
print(f'A Chapecoense esta em {times.index("Chapecoense")+1} lugar.')