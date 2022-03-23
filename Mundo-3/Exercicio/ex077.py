'''Criar um programa que tenha uma tupla com varias palavra. Depois mostrar quais são as vogais de
cada palavra'''
palavras = ('gato', 'cachorro', 'python', 'celular', 'computador', 'xicara')
print(f'{"-"*30}',end='')
for p in palavras:
    print(f'\nna palavra {p} temos:',end='')
    for letras in p:
        if letras in 'aeiou':
            print(letras,end=' ')
print(f'\n{"-"*30}')



