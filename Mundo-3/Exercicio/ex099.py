'''Faça um programa que tenha uma função chama da maior(), que receba varios paranmatros
com valores inteiros. Seu programa tem que analizar todos os valores e dizer qual é o maior'''

from time import sleep

def maior(*num):
    maior = 0
    print('~-'*30)
    print('Analisando os valores passados...')
    for pos, c in enumerate(num):
        sleep(0.3)
        print(c, end=' ')
        if pos == 0:
            maior = c
        else:
            if maior < c:
                maior = c
    print(f'Foram informados {len(num)} valores.')
    if len(num) == 0:
        print('Não a dados o suficiente para analisar!')
    else:
        print(f'O maior entre eles é {maior}')
    sleep(0.3)


maior(1, 2, 5, 8, 3, 6)
maior(7, 4, 0, 3)
maior(6, 9)
maior(9)
maior()
