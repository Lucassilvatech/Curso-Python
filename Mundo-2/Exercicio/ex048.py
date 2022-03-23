'''Mostrar a soma entre todos os multiplos de 3 que se emcontram na sequencia de 1 á 500 que são impares'''
s = 0
k = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        k = k + 1
        s = c + s
print(s,k , end=' ')
