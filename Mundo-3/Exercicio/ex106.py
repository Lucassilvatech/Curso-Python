'''Faça um mini-sistema que utilize o Interactive Help do python.
O usuario vai digitar o comando e o manual vai aparecer .
Quando o usuario digitar a palavra "FIM", o programa se encerrará.
OBS: use cores'''

def ajuda ():
    from time import sleep
    while True:
        print('\033[30;43m~-'*35)
        print('      SISTEMA DE AJUDA PyHELP')
        print('~-'*35)
        n = input('\033[mPara que comando quer ajuda:')
        if n == 'exit':
            print('\033[30;41m~-' * 35)
            print('      FINALIZANDO... ')
            sleep(1.0)
            print('      ATE LOGO!')
            print('~-' * 35)
            break
        else:
            print('\033[30;46m~-' * 35)
            print(f'      ACESSANDO SISTEMA DE AJUDA {n}!')
            print('~-' * 35)
            print('\033[m')
            sleep(0.8)
            print('\033[29;40m')
            help(n)
            print('\033[m')
ajuda()