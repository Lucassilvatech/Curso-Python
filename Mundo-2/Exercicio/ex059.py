'''ler dois valore e mostrar um menu na tela
[1] somar
[2] mutiplicar
[3] maior
[4] novos numeros
[5] sair

O progra ma devera realizar a operação solicitada em cada caso'''

'''s = 0
while s != 5:
    n = int(input('Digite um valor:'))
    v = int(input('Outro valor:'))
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] O MAIOR DIGITO \n[4]DIGITAR NOVOS NUMEROS \n[5] SAIR')

    s = int(input('Digite aqui a opção que escolheu:'))

    if s == 1:
        print(f'A soma de {n} com {v} é {n+v}  .')

    elif s == 2:
        print(f'{n} x {v} é {n*v} .')

    elif s == 3:
        print(f'O maior digito foi {max(n, v)}')
      
    elif s == 4:
        print('\033[36mOk, digite novamente.\033[m')
print('ACABOU')'''

from time import sleep
s = 0
while s != 5:
    n = int(input('Digite um valor:'))
    v = int(input('Outro valor:'))
    sair = False
    while not sair:
        print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')
        print('[1] SOMAR \n[2] MULTIPLICAR \n[3] O MAIOR DIGITO \n[4]DIGITAR NOVOS NUMEROS \n[5] SAIR')
        print('=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=')
        s = int(input('Digite aqui a opção que escolheu:'))

        if s == 1:
            print(f'A soma de {n} com {v} é {n + v}  .')

        elif s == 2:
            print(f'{n} x {v} é {n * v} .')

        elif s == 3:
            print(f'O maior digito foi {max(n, v)}')

        elif s == 4:
            print('\033[36mOk, digite novamente.\033[m')
            sair = True
        elif s == 5:
            s = 5
            sair = True
        else:
            print('Opção invalida. Tente novamente.')

print('Finalizando...')
sleep(2)
print('Programa finalizado! ATÉ A PROXIMA.')

