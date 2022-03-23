'''Ler uma frase e dizer se ela é um palíndromo, desconsiderando os espaços'''
fra = str(input('digite uma frase:')).strip().split()
fra = ''.join(fra)
n = int(len(fra))
re = ''
for c in range(n-1, -1, -1):
    re = re + fra[c]
if re == fra:
    print('Essa frase é um palíndromo!!!!!')
else:
    print('Nada incomum por aqui!')

