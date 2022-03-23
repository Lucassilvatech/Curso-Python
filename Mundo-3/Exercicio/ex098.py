'''Faça um programa que tenha uma função chamada contador que receba 3 parametros
inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens atraves da função criada:
a) De um até 10 de 1 em 1
b) De 10 até 0 de 2 em 2
c) Uma contagem personalizada.'''
from time import sleep


def contador(i, f, r):
    if i < f:
        if r == 0:
            r = 1
        print('-'*34)
        print(f'Contagem de {i} até {f} de {r} em {r} .')
        for c in range(i, f+1, r):
            sleep(0.4)
            print(c, end=' ')
        print('... END')
        print('-' * 34)
    else:
        if r <= -1:
            print('-' * 34)
            print(f'Contagem de {i} até {f} de {r} em {r} .')
            for con in range(i, f-1, r):
                sleep(0.4)
                print(con, end=' ')
            print('... END')
            print('-' * 34)
        else:
            if r == 0:
                r = 1
            print('-' * 34)
            print(f'Contagem de {i} até {f} de {r} em {r} .')
            for co in range(i, f-1, -r):
                sleep(0.4)
                print(f'{co} ', end=' ')
            print('... END')
            print('-' * 34)


#Programa principal
contador(1, 10, 0)
contador(10, 0, 2)
print('agora é sua vez de escolher os valores.')
i = int(input('Inicio:'))
f = int(input('Fim:'))
r = int(input('Razão:'))
contador(i, f, r)
