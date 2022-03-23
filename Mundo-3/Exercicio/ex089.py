'''crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada aluno e permitindo que o usuario possa ver
as notas de cada aluno individualmente.'''
alunos = []
acumulador = []

while True:
    acumulador.append(str(input('Nome do aluno:')))
    acumulador.append(float(input('Primeira nota:')))
    acumulador.append(float(input('Segunda nota:')))
    alunos.append(acumulador[:])
    acumulador.clear()
    sair = str(input('Gostaria de continuar a cadastrar alunos? [S/N]'))
    if sair in 'Nn':
        break
for pos, i in enumerate(alunos):
    for obj in i:
        pass

print(f'{"No":<6}{"Nome":>6}{"media":>10}')