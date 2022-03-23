'''criar um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas as letras minusculas
- Quantas letras ao todo( sem considerar os espaços)
- Quantas letras tem no primeiro nome'''

vareavel = str(input('Digite seu nome completo:')).strip()
print(vareavel.upper())
print(vareavel.lower())
n = int(len(vareavel))
s = int(vareavel.count(' '))
t = n - s
print(f'A quantidade de letras é {t}')
nome = vareavel.split()
k = len(nome[0])
print(f'O primeiro nome tem {k} letras')

