'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuario qual o valor
a ser sacado e o programa ira informar quantas cédulas de cada valor serão entregues.
OBS:Considere que o caixa te cedulas de R$50, R$20, R$10, R$1.'''
c50 = 50
c20 = 20
c10 = 10
c1 = 1
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Quanto deseja sacar?'))
while True:
    if c50 > valor:
        break
    c50 += 50
    cont50 +=1
c50 = c50 - 50
if c50 <= valor:
    re = valor - c50
else:
    re = valor

while True:
    if c20 > re:
        break
    c20 += 20
    cont20 +=1
c20 = c20 - 20
if c20 <= re:
    re = re - c20

while True:
    if c10 > re:
        break
    c10 += 10
    cont10 +=1
c10 = c10 - 10
if c10 <= re:
    re = re - c10

while True:
    if c1 > re:
        break
    c1 += 1
    cont1 +=1
if cont50 != 0:
    print(f'Você recebeu {cont50} cedulas de 50R$ . ')
if cont20 != 0:
    print(f'Você recebeu {cont20} cedulas de 20R$ . ')
if cont10 != 0:
    print(f'Você recebeu {cont10} cedulas de 10R$ . ')
if cont1 != 0:
    print(f'Você recebeu {cont1} cedulas de 1R$ . ')



