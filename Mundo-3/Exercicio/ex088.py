'''Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quentos
jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em lista composta.'''

from random import randint
from time import sleep

lista = []
jogo = []
n = int(input('Quantos palpites você vai querer?'))
for c in range(0,n):
    l=6
    while l > 0:
        j = randint(1,60)
        if j not in lista:
            lista.append(j)
            l -= 1

    jogo.append(lista[:])
    lista.clear()
print(f'>>> SORTEANDO {n} JOGOS...<<<')
sleep(0.8)
for pos, jogos in enumerate(jogo):
    jogos.sort()
    sleep(1.0)
    print(f'Jogo {pos+1}: {jogos}')
print('>>> BOA SORTE!!! <<<')
print('volte sempre!')
