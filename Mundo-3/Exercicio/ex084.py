'''Faça um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre
a) Quantas pessoas foram cadastradas
b) Uma listagen com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.'''

lista = list()
todo = list()
while True:
    nome = str(input('Digite seu nome:'))
    peso = float(input('Digite seu peso:'))
    todo.append(nome)
    todo.append(peso)
    lista.append(todo[:])
    todo.clear()
    while True:
        sair =str(input('gostaria de continuar? S/N'))
        if sair in 'SsNn':
            break
        else:
            print('RESPOSTA INVALIDA, tente novamente!')
    if sair in 'Nn':
        break
n = len(lista)
cem = list()
sete = list()
str = []
float = []
maxp = []
minp = []
for p in lista:
    str.append(p[0])
    float.append(p[1])
max = max(float)
min = min(float)
for pos, num in enumerate(float):
    if num >= max:
        cem.append(num)
        maxp.append(str[pos])
    elif num <= min:
        sete.append(num)
        minp.append(str[pos])
print('=' * 40)
print(f'Foram cadastradas {n} pessoas \nA lista completa é {lista} \nOs mais pesados são {maxp} com {cem} '
      f'\nOs mais leves são {minp} com {sete}')
