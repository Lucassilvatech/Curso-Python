'''Mostrar uma contagem regressiva para o estouro de fogos de artifício, indo de 0 á 10 com pausas de 1 segundo'''

import pygame
from time import sleep
for c in range(10,-1,-1):
    sleep(0.5)
    print(c)
pygame.init()
for f in range(1):
    pygame.mixer.music.load('JVLA.mp3')
    pygame.mixer.music.play()
    input()
pygame.init()
pygame.mixer.music.load('konai.mp3')
pygame.mixer.music.play()
input()

