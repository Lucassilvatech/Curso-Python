'''Crie um programa onde o usário possa digitar cinco valores numericos e cadastre-os em uma lista.
,já na posição correta de inserção (sem usar o sort()). No final mostre a lista ja ordenada'''
cont =0
lista = []
for c in range(0,5):
    num = int(input('Digite um valor:'))
    if c == 0 :
        lista.append(num)
    elif num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num >= lista[pos]:
                lista.insert(pos, num)
                break
            pos+=1
    print(f'Sua lista ja ordenada é {lista}')
