'''Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais aulguns termos .
O programa encerra quando ele disser que quer 0 tremos'''

'''pi = int(input('inicio da PA:'))
r = int(input('Razão da PA:'))
termo = pi
cont = 1
sair = False
n = 10
k = 0
while not sair:
    while cont <= n:
        print(f' {termo} ', end='')
        termo += r
        cont = cont + 1  
    print('\n',end='')
    l = str(input('Gostaria de ver mais termos? [S/N]')).strip().upper()
    if l == 'N':
        sair = True
    elif l == 'S':
        k = int(input('Quantos mais termos gostaria de ver?'))
        n = k + n
    else:
        print('OPÇÃO INVALIDA, Tente novamente.')
print('Obrigado, volte sempre!')'''

print('Calculador de PA.')
pi = int(input('Ponto inicial:'))
r = int(input('Razão:'))
termo = pi
cont = 1
k = 0
mais = 10
while mais != 0:
    k = k + mais
    while cont <= k:
        print(f'{termo}  ', end='')
        if cont != 10:
            print('-> ', end='')
        termo = termo + r
        cont += 1
    print('\n', end='')
    mais = int(input('Quantos mais termos gostaria de ver?'))
print('FIM')


