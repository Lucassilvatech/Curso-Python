import random
n1 = str(input('Nome °1 aluno:'))
n2 = str(input('Nome °2 aluno:'))
n3 = str(input('Nome °3 aluno:'))
n4 = str(input('Nome °4 aluno:'))
ordem = [n1, n2, n3, n4]
random.shuffle(ordem)
print(f'{ordem}')

