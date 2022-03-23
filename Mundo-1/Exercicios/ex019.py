# Resolvido após revisão


from random import choice
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo aluno:'))
a3 = str(input('terseiro aluno:'))
a4 = str(input('quarto aluno:'))
lista = [a1, a2, a3, a4]
s = choice(lista)
print(f'O aluno selesionado foi {s}!')