'''Faça um progra que leia 3 numeros e mostre qual é o maior entre eles'''

'''n1 = str(input('Digite um numero qualquer:'))
n2 = str(input('Mais um:'))
n3 = str(input('Outro'))
n1 = n1.replace(',','.')
n2 = n2.replace(',','.')
n3 = n3.replace(',','.')
true = float(max(n1, n2, n3))
false = float(min(n1, n2, n3))
print(f'O maior numero digitado foi {true} e o menor foi {false}')'''

'''n1 = int(input('Primeiro numero:'))
n2 = int(input('segundo numero:'))
n3 = int(input('terceiro numero:'))

if n1>n2>n3:
    maior = n1
if n2>n1>n3:
    maior = n2
if n3>n2>n1:
    maior = n3
    print(f'O maior numero é {maior} !')
if n1<n2<n3:
    menor = n1
if n2<n1<n3:
    menor = n2
if n3<n1<n2:
    menor = n3
print(f'O menor numero é {menor} !')'''

n1 = int(input('Primeiro numero:'))
n2 = int(input('segundo numero:'))
n3 = int(input('terceiro numero:'))
menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

maior = n1
if n2 > n3 and n2 > n1:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior numero é {maior} e o menor é {menor}')
