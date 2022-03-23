'''Crie uma função chamada fatorial() que receba dois parametros:
o primeiro que indique o numero a calcular e o segundo chamado show, que será um valor
logico (opicional) indicando se será mostrado ou não na tela
o processo de calculo do fatorial.'''

def fatorial (num, show=False):
    """
    Calcula o fatoril de um numero
    :param num: O numero á qual vai ser calculado o fatorial
    :param show: (opicional) para mostrar o calculo do fatorial
    :return: o valor do fatorial de um numero n
    """
    n = num
    for c in range(num-1, 0, -1):
        n *= (c)
        if show == True:
            print(f' {c+1}',end=' ')
            if c != 1:
                print(' X',end=' ')
            else:print(' = ',end=' ')

    return n


l = fatorial(5)
print(l)
help(fatorial)