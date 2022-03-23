'''Crie um programa onde o usuario possa digitar 7 valores numericos e cadastre-os em uma lista unica que
mantenha separados os valore pares e impares. No final, mostre os valores pares e impares em ordem crecente'''

lista = [[],[]]
for n in range(0,7):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitadoa foram {lista[0]} \nOs valores impares digitados foram {lista[1]} ')

