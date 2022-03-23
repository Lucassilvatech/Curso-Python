'''Crie um programa que crie uma matriz de dimenção 3 x 3 e preencha com valores lidos pelo teclado
No final, mostre a matriz na tela com a formatação correta.'''

matriz = []
acumulador = []
for c in range(0,9):
    num = int(input(f'Digite aqui o {c+1}º valor'))
    acumulador.append(num)
    matriz.append(acumulador[:])
    acumulador.clear()
print()
for pos, item in enumerate(matriz):
    if pos == 3 or pos == 6:
        print('\n',end='')
    print(f'{f"{item}"}',end='')
print()