'''refaça o ex 51 so que agora com while'''

#Feito após correção
print('Calculador de PA.')
pi = int(input('Ponto inicial:'))
r = int(input('Razão:'))
termo = pi
cont = 1
while cont <= 10:

    print(f'{termo}  ', end='')
    if cont != 10:
        print('-> ', end='')
    termo = termo + r
    cont += 1
    if cont == 11:
        print('FIM')









