'''desenvolva um programa que leia quatro valores pelo teclado e garde-os em um tupla.No final
mostre:
a) quantas vezes apareceu o valor 9 .
b) Em que posição foi digitado o primeiro valor 3 .
c) Quais foram os números pares.'''

numeros = (int(input('digite um valor:')),int(input('digite um valor:')),
        int(input('digite um valor:')),int(input('digite um valor:')),)

print(f'O numero 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O primeiro numero 3 foi digitado na posição {numeros.index(3)+1}')
else:
    print('O valor 3 não foi digitado nem uma vez!')
print('Os numeros pares são:',end='')
for n in numeros:
    if n % 2 == 0:
        print(n,end=' ')