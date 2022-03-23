'''Crie um programa que vai ler varios numeros e colocar em uma lista.
Depois disso, crie duas listas que vão conter apenas os valores pares e os valores impares
digitados respecivamente.
no final mostre as 3 listas'''
lista = []
while True:
    num = int(input('Digite um numero:'))
    lista.append(num)
    sair = str(input('Gostaria de continuar? S/N'))
    if sair in 'Nn':
        break
pares = []
impares = []
for item in lista:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print(f'A lista completa é {lista} \nA lista dos numeros pares é {pares} \nA lista dos numeros impares é {impares}')

