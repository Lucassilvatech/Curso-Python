'''Aprimore o desafio anterior mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha'''

pares = 0
coluna3 = 0
linha2 = []
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para a posição [{l},{c}:^5]'))
print('-='*30 )
for l, num in enumerate(matriz):
    for c, nume in enumerate(num):
        if nume % 2 == 0:
            pares += nume
        if l == 1:
            linha2.append(nume)
        if c == 2:
            coluna3 += nume
        print(f'[{nume}]', end=' ')
    print()
maior = max(linha2)
print('-='*30 )
print(f'Os valores pares são {pares} .\n'
      f'A soma dos valores da terceira coluna é {coluna3} .\n'
      f'O maior valor da segunda linha é {maior}')


