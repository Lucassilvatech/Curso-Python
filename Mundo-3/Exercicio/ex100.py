'''Faça um programa que tenha uma lista chamada numeros e duas funções chamadas
sorteia() e somapar() aprimeira função vai sortear 5 numeros e vai colocalos dentro da lista
e a segunda função vai mostrar a soma de todos os numeros pares sorteados pela função anterior'''

numeros = list()

def sorteia (lista):
    from random import randint
    from time import sleep
    print('Os valores sorteados foram:')
    for c in range(0, 5):
        n = randint(0,9)
        sleep(0.3)
        print(n,end=' ')
        if c == 4:
            sleep(0.3)
            print('PRONTO!')
        lista.append(n)
    sleep(0.7)

def somapar (lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares em {lista} é igual á {soma}')


k = []
sorteia(k)
somapar(k)