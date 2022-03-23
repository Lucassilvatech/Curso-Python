'''crie um programa que leia o nome de uma pessoa e diga se tem 'Silva' nesse nome'''

nome = str(input('digite seu nome completo:')).strip()
nome1 = nome.lower()
nome2 = nome1.split()
print(f'{"silva"in nome2}')

