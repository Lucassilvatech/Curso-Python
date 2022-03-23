'''Crie um programa que vai ler varios numeros e colocar em uma lista. Depois mostre:
a) Quantos numeros foram digitado.
b) A lista ordenada de forma decresente.
c) Se o valor 5 foi digitado e se estar ou não na lista'''

valores = []
while True:
    n = int(input('Digite um valor:'))
    valores.append(n)
    sair = str(input('Gostaria de continuar? S/N'))
    if sair in 'Nn':
        break
n = len(valores)
valores.sort(reverse=True)
print('-'*30)
print(f'Foram digitados {n} numeros')
print('A lista em ordem decresente é  ',end='')
for num in valores:
    print(f'{num}...',end='')
if 5 in valores:
    print('\nO numero 5 faz parte da lista!')
else:
    print('\nO numero 5 não faz parte da lista!')
