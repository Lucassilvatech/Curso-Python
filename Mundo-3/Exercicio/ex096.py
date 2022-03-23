'''Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a area do terreno.'''


def area(a, b):
    s = a * b
    print(f'Seu terreno tem {s}M²')


a = float(input('Lagura do terreno:'))
b = float(input('comprimento do terreno:'))
area(a,b)