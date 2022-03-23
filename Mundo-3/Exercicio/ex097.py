'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro
e mostre uma mensagem com tamanho adaptavel.'''


def escreva(texto):
    m = len(texto) + 4
    print('-' * m)
    print(f'  {texto}')
    print('-' * m)


escreva(str(input('Digite uma frase:')))