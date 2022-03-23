'''Crie um programa que leia o nome de uma cidade e dida se ela começa com 'santo' ou não '''

'''nome = str(input('digite o nome da sua cidade:').strip())
nome = nome.lower()
nome2 = nome.split()
nome3 = nome2[0]
print(f'O nome dessa cidade começa com Santo? {"santo"in nome3}')'''

city = str(input('Qual nome da sua cidade:')).strip()
city = city.lower()
print(city[:5] == 'santo')