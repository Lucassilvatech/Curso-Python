'''Ler 6 numero inteiro e mostrar a soma dos valores que forem pares, se não desconsidere.'''
s = 0
for c in range(1,7):
    n = int(input('Digite um valor:'))
    if n % 2 == 0:
        s = s + n

print(f'A soma dos valores peres deu {s}')