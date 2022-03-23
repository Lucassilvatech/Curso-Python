'''Tem que ler o nome completo de uma pessoa e mostrar seu primeiro nome e o ultimo separadamente '''

'''nome = input('Digite seu nome completo:')
nome = nome.title()
n1 = nome.split()
n2 = n1[0]
n3 = nome.split()
n4 =n3[-1]
print(f'Seu primeiro nome é {n2} \ne seu ultimo nome é {n4}.')'''

n = str(input('digite seu nome:')).strip()
n = n.title()
nome = n.split()
print(f'Seu primeiro nome é {nome[0]} \nSeu ultimo nome é {nome[len(nome)-1]} ')