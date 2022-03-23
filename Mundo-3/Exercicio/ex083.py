'''Crie um programa onde o usuario digite uma expreção matematica qualquer usando parênteses
Seu aplicativo deverá analisar se a expressão esta com os parênteses abertos e fechados na ordem correta.'''

'''expreção =  []
di = es = 0
n = str(input('Digite uma expressão que contenha parenteses:'))

for item in n:
    if item == '(':
        di +=1
    elif item == ')':
        es += 1
if di == es:
    print('Essa expressão esta correta!')
else:
    print('Essa expreção esta incorreta!')'''

#feito apos correção

lista = []
n = str(input('Digite uma expressão que contenha parenteses:'))
for item in n:
    if item == '(':
        lista.append('(')
    elif item == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Essa expressão esta correta!')
else:
    print('Essa expreção esta incorreta!')









